// src/handlers.rs
// Handler to perform SELECT
// Define an asynchronous function that takes web::Data<SqlitePool> to
// access the database pool and performs a SELECT query.

use actix_web::{web, HttpResponse, Responder};
use sqlx::{SqlitePool, FromRow};

#[derive(Debug, FromRow)]
#[derive(serde::Serialize)]
struct Entry {
    url: String,
    datatime: String,
    day: String,
    hour: String,
    site: String,
    size: i64
}

pub async fn get_entries(pool: web::Data<SqlitePool>) -> impl Responder {
    match sqlx::query_as::<_, Entry>("select url, datatime, day, hour, site, size from halpha order by datatime")
        .fetch_all(pool.get_ref())
        .await
    {
        Ok(entries) => HttpResponse::Ok().json(entries),
        Err(e) => HttpResponse::InternalServerError().body(format!("Database error: {:?}", e)),
    }
}

