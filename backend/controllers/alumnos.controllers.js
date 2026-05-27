import { Tabla } from "../models/alumnos.model.js";
Tabla.create({
    nombre : "coffe",
    edad : 20,
    materia : "Todas"

})
export const test =()=>console.log("Llamando el controladoren app")