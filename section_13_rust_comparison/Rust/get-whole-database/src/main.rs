// JSON dump of large database
// Output turns up at URL :
// http://localhost:8002/getWholeDatabase
//
use actix_web::{web, App, HttpServer};
use sqlx::SqlitePool;

mod db;       // See db.rs for database connection module
mod handlers; // Handlers are in handlers.rs module

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let pool: SqlitePool = db::init_db().await;
    let pool_data = web::Data::new(pool);

    HttpServer::new(move || {
        App::new()
            .app_data(pool_data.clone()) // Make pool available to handlers
            .service(web::resource("/getWholeDatabase").to(handlers::get_entries))
    })
    .bind(("localhost", 8002))?
    .run()
    .await
}



