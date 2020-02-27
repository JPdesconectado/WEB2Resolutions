   /* 	DESAFIO!!!
    	Implemente um algoritmo para inverter a ordem de uma string em sua
    	linguagem de programacao favorita. Nao use funcoes/metodos prontos
    	
   */
    	
    	String ordem = "tentativa";
    	int tam = ordem.length();
    	char[] inversao = new char[tam];
    	int j = 0;
    	
    	for (int i = tam - 1; i >= 0; i--) {
    		inversao[j] = ordem.charAt(i);
    		j++;
    	}
    	
    	System.out.println(inversao);
