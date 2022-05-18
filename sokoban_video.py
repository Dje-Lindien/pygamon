
PImage naruto;

PImage crystal;
PImage caisse;
PImage brique;

int level[][] = {
    {0,0,1,1,1,0,0,0},
    {0,0,0,0,1,0,0,0},
    {0,0,0,0,1,1,1,1},
    {0,0,0,0,0,0,0,1},
    {0,0,0,0,0,1,1,1},
    {0,0,0,0,0,1,0,0},
    {0,0,0,0,0,0,0,0},
};

void setup(){
    size(600,600);

    perso = loadImage("naruto.jpg");

    crystal = loadImage("crystal.jpg");
    caisse = loadImage("caisse.png");
};

void draw(){

}

void afficheMap(){
    for(int i = 0; i < 8;i++){
        for(int j = 0; j < 8;i++){
            
        }
    }
}