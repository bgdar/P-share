
use actix_web::{App,web, HttpServer};
use tera::Tera;

//setup module
mod controller;
mod models;
mod config;

use controller::*;

#[actix_web::main]
async fn main() ->  std::io::Result<()> {
    println!("web actix denngan ");
    //inisialisasikan views/
    //let tera = Tera::new("views/**/*").unwrap();
    let tera = Tera::new("src/views/**/*.html").unwrap();


    println!("server berjalan di 127.0.0.1:5000");
    HttpServer::new(move||{
        App::new()
           .app_data(web::Data::new(tera.clone())) 
            .service(home_controller::index)
            .service(user_controller::index)
            //menggunakn file public 
            .service(actix_files::Files::new("/public", "public").show_files_listing())
            
    })
    .bind("127.0.0.1:5000")?
    .run()
    .await
}
