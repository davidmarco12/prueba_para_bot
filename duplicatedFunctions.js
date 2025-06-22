// Función 1: Calcular el área de un cuadrado
function areaCuadrado1(lado) {
  const area = lado * lado;
  console.log("Área del cuadrado: " + area);
}

// Función 2: Calcular el área de otro cuadrado (misma fórmula)
function areaCuadrado2(lado) {
  const area = lado * lado;
  console.log("Área del cuadrado: " + area);
}

// Función 3: Calcular la suma de los primeros N números naturales
function sumaHastaN1(n) {
  let suma = 0;
  for (let i = 1; i <= n; i++) {
    suma += i;
  }
  console.log("Suma hasta " + n + ": " + suma);
}

// Función 4: Calcular la suma hasta otro número (== )
function sumaHastaN2(m) {
  let suma = 0;
  for (let i = 1; i <= m; i++) {
    suma += i;
  }
  console.log("Suma hasta " + m + ": " + suma);
}

// Función 5: Calcular promedio de tres notas
function promedioNotas1(a, b, c) {
  const promedio = (a + b + c) / 3;
  console.log("Promedio: " + promedio);
}

// Función duplicada sin sentido
function promedioNotas2(x, y, z) {
  const promedio = (x + y + z) / 3;
  console.log("Promedio: " + promedio);
}
