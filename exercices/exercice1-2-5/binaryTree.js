class Noeud {
    constructor(val) {
        this.valeur = val;
        this.gauche = undefined;
        this.droite = undefined;
        this.parent = undefined;
    }

    // Affiche la valeur du noeud et la valeur de ses deux enfants et de son parent
    toString() {
        var out = "Noeud " + this.valeur + ":  L";

        this.gauche === undefined ? out += "-" : out += this.gauche.valeur;
        out += " R";

        this.droite === undefined ? out += "-" : out += this.droite.valeur;
        out += " P";

        this.parent === undefined ? out += "-" : out += this.parent.valeur;
        console.log(out);
    }
}
class Arbre {
    constructor() {
        this.racine = undefined;
    }


    trouverNoeudArbre(node, valeur) {
        if (node != undefined) {
            if(node.valeur === valeur) {
                return node;
            } else if (node.valeur > valeur) {
                return this.trouverNoeudArbre(node.gauche, valeur);
            } else if (node.valeur < valeur) {
                return this.trouverNoeudArbre(node.droite, valeur);
            } 
        }
        return undefined;
    }
    //Méthode pour trouver une valeur donnée dans un arbre binaire de recherche
    trouverNoeud(valeur) {
        if(this.racine === undefined)
            return false;
        return this.trouverNoeudArbre(this.racine, valeur);
    }

    ajouterNoeudArbre(noeud, valeur) {
        // console.log("ajouterNoeud(node, valeur) ");
        if (noeud !== undefined) {
            if (valeur < noeud.valeur) {
                if(noeud.gauche === undefined) {
                    noeud.gauche = new Noeud(valeur);
                    noeud.gauche.parent = noeud;
                } else {
                    this.ajouterNoeudArbre(noeud.gauche, valeur);
                }
            }
            else if (valeur > noeud.valeur) {
                if(noeud.droite === undefined) {
                    noeud.droite = new Noeud(valeur);
                    noeud.droite.parent = noeud;
                } else {
                    this.ajouterNoeudArbre(noeud.droite, valeur);
                }
            } else {
                console.log("Node already exists");
            }
        }
    }

    ajouterNoeud(valeur) {
        if (this.racine === undefined) {
            this.racine = new Noeud(valeur);
        } else {
            this.ajouterNoeudArbre(this.racine, valeur)
        }
    }

    
    minValue(noeud) {
        if (noeud.gauche === undefined)
              return noeud.valeur;
        else
              return this.minValue(noeud.gauche);
    }

    maxValue(noeud) {
        if (noeud.droite === undefined)
              return noeud.valeur;
        else
              return this.maxValue(noeud.droite);
    }
    //Méthode pour supprimer un noeud
    supprimerNoeudArbre(node, valeur) {
        if (valeur < node.valeur) {
            if (node.gauche !== undefined)
                  return this.supprimerNoeudArbre(node.gauche, valeur);
            else
                  return false;
        } else if (valeur > node.valeur) {
            if (node.droite !== undefined)
                  return this.supprimerNoeudArbre(node.droite, valeur);
            else
                  return false;
        } else {
                if (node.gauche !== undefined && node.droite !== undefined) {
                    node.valeur = this.maxValue(node.gauche);
                    this.supprimerNoeudArbre(node.gauche, node.valeur);
                } else if (node.parent.gauche === node) {
                    node.parent.gauche = (node.gauche !== undefined) ? node.gauche : node.droite;
                } else if (node.parent.droite === node) {
                    node.parent.droite = (node.gauche !== undefined) ? node.gauche : node.droite;
                }
                return true;
        }
    }

    supprimerNoeud(valeur) {
        if(this.racine.valeur === valeur) {
            this.racine = undefined;
        } else {
            this.supprimerNoeudArbre(this.racine, valeur);
        }
         
    }


    //Méthode pour afficher l’arbre selon un parcours infixe
    //Cette méthode doit retournée un tableau contenant la valeur des noeuds
    infixeNoeud(noeud, array) {
        if(noeud !== undefined) {
            if(noeud.gauche !== undefined) {
                this.infixeNoeud(noeud.gauche, array);
            }
            if(noeud.valeur !== undefined) {
                array.push(noeud.valeur);
            }   
            if(noeud.droite !== undefined) {
                this.infixeNoeud(noeud.droite, array);
            }       
        }
    }

    infixe() {
        var array = [];
        if(this !== undefined) {
            if(this.racine !== undefined) {
                this.infixeNoeud(this.racine, array);
                return array;
            }
        }
        
    }

    //Méthode pour afficher la valeur d'un noeud à partir de sa valeur
    printNoeud (valeur) {
        let noeud = this.trouverNoeud(valeur);
        if (noeud !== undefined) noeud.toString();
    }
}

let a = new Arbre();	
a.printNoeud(33);	
a.printNoeud(35);	
a.printNoeud(46);	 
a.ajouterNoeud(24);	 
a.ajouterNoeud(11);	 
a.ajouterNoeud(33);	 
a.ajouterNoeud(13);	 
a.ajouterNoeud(40);	 
a.ajouterNoeud(46);	 
a.ajouterNoeud(14);	 
a.ajouterNoeud(21);	 
a.ajouterNoeud(12);	 
a.ajouterNoeud(10);	 
a.ajouterNoeud(31);	 
a.ajouterNoeud(35);	 
a.ajouterNoeud(32);	 
 	 
a.supprimerNoeud(40);	 
a.printNoeud(33);	 
a.printNoeud(35);	 
a.printNoeud(46);

//Noeud 33:  L31 R35 P24
//Noeud 35:  L- R46 P33
//:pmNoeud 46:  L- R- P35