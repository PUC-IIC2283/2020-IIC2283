Este problema se puede resolver con una técnica conocida como [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html). Pueden encontrar otras explicaciones decentes de la técnica [aquí](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14/editorial) y [aquí](https://jeffreyxiao.me/blog/divide-and-conquer-optimization). A continuación una explicación de cómo usar esta idea de forma concreta en el problema.

Si definimos K como la cantidad de puntos de acceso a instalar, el problema se puede repensar como particionar los N pueblos en K+1 grupos consecutivos delimitados por los puntos de acceso. El primer grupo va desde el pueblo 0 hasta el pueblo donde ponemos el primer punto de acceso, el segundo grupo va desde el anterior + 1 hasta el pueblo donde ponemos el segundo punto de acceso, ..., y el grupo K+1 desde el pueblo donde ponemos el último punto de acceso + 1 hasta el último pueblo.

Notar que el costo óptimo de un grupo queda completamente definido dado los índices donde comienza y termina. Si un grupo comienza en el pueblo i y terminar en el pueblo j (i <= j), podemos definir

> cost(i, j) = el costo óptimo de proveer de internet a los pueblos i, i+1, i+2, ..., j suponiendo que en i y en j+1 hay puntos de acceso (hay que tener cuidado con los casos bordes del primer y último grupo, ya que ahí no hay punto de acceso a la izquierda y derecha respectivamente).

Notar que cost(i, j) se puede calcular en O(1), puesto que sabemos que la mitad de los pueblos van a preferir el borde izquierdo, la otra mitad el borde derecho, por lo que el costo queda dado por dos sumatorias que se pueden calcular en O(1) si hacemos algunos precomputos convenientemente al principio.

Entendiendo lo anterior, ahora veamos cómo podemos atacar el problema con programación dinámica. La clave está en pensarlo como la forma óptima de particionar N pueblos en K+1 grupos consecutivos, y en cada paso ir decidiendo el tamaño del último grupo y resolviendo recursivamente lo que me sobra a la izquierda del último grupo. Concretamente:

> DP(k, i) = el costo mínimo de agrupar los pueblos 0, 1, 2, ..., i en (k+1) grupos (i.e. de instalar k puntos de acceso) suponiendo que en i+1 hay un punto de acceso (a menos que i sea N-1, en cuyo caso no hay punto de acceso a la derecha)

Esto se puede plantear recursivamente como:

> DP(0, i) = cost(-1, i)  # -1 porque no hay punto de acceso al principio

> DP(k,i) = min { cost(j, i) + DP(k-1, j-1) para j = k-1 ... i } si k > 0

Notar que este DP tiene N^2 estados y calcular cada estado requiere O(N) cómputo. Por lo tanto, la complejidad es O(N^3). ¿Se puede hacer mejor?

Sí, podemos aplicar _divide and conquer optimization_ (la técnica spoileada al principio). Muy en resumen, la clave de la técnica D&C para DP es achicar el rango de búsqueda del j óptimo en la recurrencia del DP:

> DP(k,i) = min { cost(j, i) + DP(k-1, j-1) para j = k-1 ... i } si k > 0

En vez de hacer el for loop desde j=k-1 hasta j=i, se hace un for loop desde j=j1 hasta j=j2, donde j1 y j2 son cotas "inteligentes". La recurrencia quedaría como:

> DP(k,i) = min { cost(j, i) + DP(k-1, j-1) para j = j1...j2 } si k > 0

¿De dónde salen j1 y j2?

Vienen de la siguiente observación. Sea:
> opt_j(k, i) = el primer índice j de izquierda a derecha donde DP(k,i) logra el óptimo.

Ahora pensemos en un k fijo y sólo variemos el i (esto sería resolver la fila k-ésima de la tabla del DP). Si se cumple que opt_j(k,i) <= opt_j(k,i+1), entonces podemos usar opt_j(k,i-1) y opt_j(k,i+1) para acotar el rango de búsqueda del j óptimo para DP(k,j).

La idea de D&C DP es llenar las filas de la tabla del DP en orden (la fila k=0, k=1, etc.). La fila k=0 es el caso base, así que se puede llenar trivialmente con la función cost(i,j). Cada siguiente fila se puede llenar con una función recursiva con complejidad O(N log N). Como son N filas, esto da una complejidad final O(N^2 log N).

Para llenar la k-ésima fila en O(N log N), se usa _divide and conquer_: nos paramos en la mitad de la fila, encontramos el j óptimo del problema de al medio, y luego seguimos resolviendo recursivamente la mitad izquierda y la mitad derecha propagando ese j óptimo como cota derecha/izquierda respectivamente. Como este procedimiento tiene a lo más O(log N) de profundidad de recursión, y en cada nivel se hace a lo más O(N) trabajo, el costo total es O(N log N).

Para más detalles de la técnica, revisar los links compartidos al principio.