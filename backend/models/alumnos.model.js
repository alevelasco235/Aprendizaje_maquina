import {Schema, model} from 'mongoose'


const Esqueleto_de_tabla = new Schema({
    nombre =String,
    edad = Number,
    materia = String
})
const Tabla = new model("Tabla de alumnos reprobados"), Esqueleto_de_tabla