
// An asynchronous function to initialize the database connection
// pool. This pool will manage database connections efficiently.
// Need to have .env file set up.
//
use sqlx::{sqlite::SqliteConnectOptions, SqlitePool};
use std::env;

pub async fn init_db() -> SqlitePool {
    // Usually would use dotenvy::dotenv().ok() to load .env
    dotenvy::from_filename("DotEnv").ok(); // Load env file
    let database_file = env::var("DATABASE_FILE")
        .expect("DATABASE_FILE must be set");

    let options = SqliteConnectOptions::new()
        .filename(database_file);

    SqlitePool::connect_with(options).await.expect("Failed to connect to db")

}

