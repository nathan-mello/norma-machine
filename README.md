# norma-machine



- Norma (Number Theoretic Register Machine) é uma máquina universal definida por Bird (Bird 1976). A memória é composta por registros infinitos e os conjuntos de entradas e saídas são números inteiros não nulos. As operações e testes definidos pela Norma são os naturais: adicionar e subtrair uma unidade ao registro e verificar se um registro é zero. Podemos notar que, na definição da subtração sobre o registro A, supõe-se que, quando o registro A já é nulo, o valor nulo permanece em A.



#### instruções de uso

- código executado da versão Python 3.9.4

- As operações são feitas de dois em dois

- Preferencialmente coloque as operações de multiplicação primeiro

- Coloque os valores negativo entre colchete [-4] 

- Exemplo de entradas validas: 

  10-[-4]           [-10]-4            [-10]-[-4]          10-4               4-[-10] 
  [-4]-10            10+59            [-4]-[-10]          4-10               5*8-9 

- Exemplo de entradas NÃO validas: 

  ][-9+5          htosn                *-989--        [-5-9]+234