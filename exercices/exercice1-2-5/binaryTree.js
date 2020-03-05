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

    maxValue(noeud) {
        if (noeud.droite === undefined)
              return noeud.valeur;
        else
              return this.maxValue(noeud.droite);
    }

    minValue(noeud) {
        if (noeud.gauche=== undefined)
              return noeud.valeur;
        else
              return this.minValue(noeud.gauche);
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
                    node.valeurGauche = this.minValue(node.gauche);
                    node.valeurDroite = this.maxValue(node.droite);

                    if (node.valeur - node.valeurGauche < node.valeurDroite - node.valeur) {
                        this.supprimerNoeudArbre(node.gauche, node.valeurGauche);
                        node.valeur = node.valeurGauche;
                    } else {
                        this.supprimerNoeudArbre(node.droite, node.valeurDroite);
                         node.valeur = node.valeurDroite;
                    }

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