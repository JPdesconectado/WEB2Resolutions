   /* 	DESAFIO!!!
    	Crie uma lista com os numeros de 0 ate 99999999999999999999999999. 
		Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
		OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
   */
    	List<Integer> lista = new ArrayList<>();
    	
    	for (int i = 0; i < 99999; i++) {
    		lista.add(i);
    	}
    	
    	for (int j = 0; j < lista.size(); j++) {
    		if (j % 5 == 0) {
    			System.out.println("O primeiro multiplo de 5 é: " + j);
    			break;
    		}
    	}
