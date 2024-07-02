A la hora de hacer el prompt se debe solicitar

Editor: Nombre de la persona 
Orcid: ID de investigador de la persona 
Affiliation: Tanto lugar de nacimiento como sitio donde trabaja el editor
Role:Rol del miembro editorial, al no ser requerido se toma como Null
Journal:Nombre de ka revista
Publisher: Publisher de la revista, al no ser requerida, se toma como null
Issn: Id de la revista
Date: Fecha en la que se almacena la información del miembro editorial
Url: URL que muestra la información de los miembros editoriales de cada web

Esta información se almacena en tres archivos, teniendo en cuenta la afiliación del miembro editorial "membersGPTAfiliacion".
Se almacenan todos los miembros editoriales de cada web sin tener en cuenta la falta de afiliación "membersGPT" 
Se utiliza el último archivo Excel "muestra_openeditors" para comprobar el funcionamiento del modelo con cuatro páginas externas a aquellas almacenadas en el excel de Origen

A la hora de ejecutar el programa se requiere la utilización de los tres archivos python principales:

- TFGMain.py: Permite la eejcución del sistema.
- FuncionesTFG.py: Archivo python en el que se cumplen todas las funcionalidades del modelo.
- Variables.env: Utilizada para almacenar toda la información requerida para el funcionamiento del sistema.


