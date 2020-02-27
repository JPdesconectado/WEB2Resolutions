   /* 	1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    	2) Agora faca sem utilizar uma terceira variavel temporaria.
    	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
    	
    */
    	
    	// 1
    	int x = 10;
    	int y = 25;
    	int aux;
    	
    	System.out.println("Valor de X: " + x);
    	System.out.println("Valor de Y: " + y);
    	System.out.println("Mudando valores...");
    	aux = x;
    	x = y;
    	y = aux;
    	System.out.println("Encerrado.");
    	System.out.println("Valor de X: " + x);
    	System.out.println("Valor de Y: " + y);
    	
    	
    	System.out.println("------- QUESTÃO DOIS ----------");
    	// 2
    	int x2 = 12;
    	int y2 = 50;
    	
    	System.out.println("Valor de X: " + x2);
    	System.out.println("Valor de Y: " + y2);
    	System.out.println("Mudando valores...");
    	
    
    	x2 = x2 + y2;
    	y2 = x2 - y2;
    	x2 = x2 - y2;

    	System.out.println("Encerrado.");
    	System.out.println("Valor de X: " + x2);
    	System.out.println("Valor de Y: " + y2);
