1. ¿Qué es el principio SRP (Single Responsibility Principle)?

El principio SRP (Single Responsibility Principle) es uno de los principios SOLID de la programación orientada a objetos. Este principio establece que una clase o módulo debe tener una única responsabilidad o razón para cambiar, es decir, debe encargarse de una única tarea o función. Al aplicar SRP, se busca que el código sea más fácil de mantener, entender y modificar, ya que cada clase se enfoca en una única preocupación, lo que también facilita la prueba y depuración.

2. ¿Por qué es importante validar la entrada del usuario? Relaciónalo con OWASP.

La validación de la entrada del usuario es crucial para garantizar la seguridad de una aplicación. Si no validamos correctamente la entrada, podemos estar abriendo la puerta a vulnerabilidades como inyecciones de SQL, ataques XSS, o incluso ejecución de código malicioso. OWASP (Open Web Application Security Project) proporciona una lista de buenas prácticas para la seguridad de las aplicaciones web, y una de las recomendaciones clave es precisamente validar todas las entradas de los usuarios. Validar datos ayuda a prevenir que los atacantes introduzcan información inesperada o maliciosa que pueda comprometer la aplicación o sus usuarios.

3. ¿Qué beneficios tiene separar el código en funciones o clases?

Separar el código en funciones o clases tiene varios beneficios importantes:
  •	Reusabilidad: El código modularizado se puede reutilizar en diferentes partes de la aplicación, lo que evita la duplicación.
  •	Mantenibilidad: Cada función o clase tiene una responsabilidad clara y limitada, lo que facilita la identificación de errores y el mantenimiento del código.
  •	Escalabilidad: Un código bien estructurado puede ampliarse y modificarse sin afectar otras partes del sistema.
  •	Facilita la colaboración: Al dividir el trabajo en unidades más pequeñas, diferentes desarrolladores pueden trabajar en diferentes funciones o clases sin interferir demasiado en el trabajo de otros.

4. ¿Qué es Clean Code y cómo se diferencia de un código que solo "funciona"?

Clean Code se refiere a un código que es fácil de leer, entender y mantener. Es un código que está bien organizado, con nombres descriptivos para variables y funciones, y sigue principios que facilitan su comprensión y extensión. A diferencia de un código que "solo funciona" (que podría ser funcional pero desordenado, sin comentarios, o difícil de modificar), el Clean Code está diseñado pensando en el futuro, en la colaboración de otros desarrolladores y en la sostenibilidad del código. Es más fácil de depurar, probar y mejorar con el tiempo.

5. Enumera tres errores comunes que debemos evitar al pedir datos por consola.
 
  1.	No validar la entrada del usuario: Es importante verificar que los datos ingresados sean correctos y del tipo esperado. No hacerlo puede llevar a errores en el programa o vulnerabilidades.
  2.	No manejar excepciones o errores: Si el usuario ingresa algo inesperado (como texto cuando se espera un número), el programa podría fallar. Es esencial manejar estas situaciones con mensajes de error apropiados y           pedir   al usuario que reingrese los datos.
  3.	No proporcionar instrucciones claras: Si no se dan instrucciones claras sobre qué tipo de datos se esperan (por ejemplo, "ingrese un número de teléfono" o "escriba un nombre"), el usuario puede introducir datos             incorrectos, lo que puede afectar el funcionamiento del programa.
