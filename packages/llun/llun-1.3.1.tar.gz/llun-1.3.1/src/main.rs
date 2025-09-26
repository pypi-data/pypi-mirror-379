use clap::{Parser, Subcommand};
use figment::{
    Figment,
    providers::{Format, Serialized, Toml},
};
use serde::{Deserialize, Serialize};
use std::path::PathBuf;

pub mod api_client;
pub mod data;
pub mod files;
pub mod formatters;
pub mod rules;
pub mod per_file_ignorer;

pub use api_client::{AvailableScanner, PromptManager, ScannerManager};
pub use data::DEFAULT_CONFIG;
pub use files::FileManager;
pub use formatters::{OutputFormat, OutputManager};
pub use rules::RuleManager;
pub use per_file_ignorer::PerFileIgnorer;

/// CLI for the application
#[derive(Parser)]
#[command(name = "llun")]
#[command(about = "LLM backed technical strategy tool", long_about = None)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Commands,
}

#[derive(Subcommand)]
pub enum Commands {
    #[command(about = "Run LLM based architectural survey")]
    Check(Args),
}

/// Arguments for the check cli command
/// NOTE: skip_serialisation_if must be set to allow toml values to
/// not be overwritten by emty values
#[derive(Parser, Debug, Serialize, Deserialize)]
pub struct Args {
    /// paths from root to desired directory or specific file
    #[serde(skip_serializing_if = "Vec::is_empty")]
    path: Vec<PathBuf>,

    /// paths otherwise targetted by 'path' that should be skipped from scanning
    #[arg(short, long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    exclude: Vec<PathBuf>,

    /// rules to utilise in the scan (overrides default values)
    #[arg(short, long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    select: Vec<String>,

    /// rules to add to the default to utilise in the scan
    #[arg(long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    extend_select: Vec<String>,

    /// rules to ignore from the default list
    #[arg(short, long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    ignore: Vec<String>,

    /// openai model to use under the hood
    #[arg(short = 'M', long)]
    #[serde(default, skip_serializing_if = "Option::is_none")]
    model: Option<String>,

    /// default ignore all files in the gitignore, to avoid leaking secrets etc...
    #[arg(short, long, action = clap::ArgAction::SetTrue)]
    #[serde(default)]
    no_respect_gitignore: bool,

    /// type of output to give
    #[arg(short, long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    output_format: Vec<OutputFormat>,

    /// llm provider
    #[arg(long)]
    #[serde(default, skip_serializing_if = "Option::is_none")]
    provider: Option<AvailableScanner>,

    /// user provided context (i.e. commit message) to help llun understand the point
    #[arg(short, long)]
    #[serde(default, skip_serializing_if = "Option::is_none")]
    context: Option<String>,

    /// utilise USC to improve the reliability of the model response
    #[arg(long, action = clap::ArgAction::SetTrue)]
    #[serde(default)]
    production_mode: bool,

    /// files to ignore certain rule violations on i.e. 'main.py::RULE01'
    #[arg(long)]
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    per_file_ignores: Vec<String>,
}

#[allow(dead_code)] // the codes not dead, just uncalled in the repo
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();
    let rule_manager = RuleManager::new()?;
    let scanner_manager = ScannerManager::new()?;
    let output_manager = OutputManager::new();

    match cli.command {
        Commands::Check(cli_args) => {
            let config: Args = Figment::new()
                .merge(Toml::string(DEFAULT_CONFIG)) // default values are set in the data file
                .merge(Toml::file("pyproject.toml").nested())
                .merge(Toml::file("llun.toml"))
                .merge(Serialized::defaults(cli_args))
                .select("tool.llun")
                .extract()?;

            let per_file_ignorer = PerFileIgnorer::new(config.per_file_ignores)?;

            let files = FileManager::load_from_cli(
                config.path,
                config.exclude,
                config.no_respect_gitignore,
            )?;
            let rules =
                rule_manager.load_from_cli(config.select, config.extend_select, config.ignore)?;

            let prompt_manager = PromptManager::new(&rules, &files, &config.context)?;
            let model_response = scanner_manager
                .run_scan(
                    &prompt_manager.system_prompt_scan,
                    &prompt_manager.user_prompt,
                    &config.model.expect("A model must be provided"),
                    &prompt_manager.system_prompt_consistency,
                    config.provider.expect("A provider must be provided."),
                    config.production_mode,
                )
                .await?;

            let filtered_response = per_file_ignorer.apply_ignores(model_response);

            output_manager.process_response(&filtered_response, &config.output_format)?
        }
    }
    Ok(())
}
