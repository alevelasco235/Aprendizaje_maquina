import mongoose from "mongoose";//Libreria para conexion de base de datos
import express from "express";//libreria para crear servidores
import cors from "cors";//libreria para darle seguridad al servidor 
import dotenv from "dotenv";//Libreria para configurar el documento .env


dotenv.config();
mongoose.connect(process.env.url_bd)
.then(()=>console.log("Todo jala chido en la base de datos"))
.catch((error)=> console.log("No esta jalando esta madre"))



//servidor
const app = express;
app.use(cors());
app.listen(() =>console.log("Esta jalando el servidor, no escucha borroso"))