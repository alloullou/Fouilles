public class Arrondissement {
	
	private int num;
	private int taille;
	private String position;


	public Arrondissement(int num, int taille, String position){
		this.num = num;
		this.taille = taille;
		this.position = position;
	}

	public int getNum(){
		return num;
	}
	public void setNum(int num){
		this.num = num;
	}
	public int getTaille(){
		return taille;
	}
	public void setTaille(int taille){
		this.taille = taille;
	}
	public String getPosition(){
		return position;
	}
	public void setPosition(String position){
		this.position = position;
	}

}