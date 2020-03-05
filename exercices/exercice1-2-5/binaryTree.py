class Noeud:
    def __init__(self, v, parent=None):
        self.valeur = v
        self.parent = parent
        self.gauche = None
        self.droite = None

    def toString(self):
        out = "Noeud " + str(self.valeur) + ":  L";
        if (self.gauche is None):
            out += "-"
        else:
            out += str(self.gauche.valeur)
        out += " R";
        if (self.droite is None):
            out += "-"
        else:
            out += str(self.droite.valeur)
        out += " P";
        if (self.parent is None):
            out += "-"
        else:
            out += str(self.parent.valeur)

        print(out)

    def trouverNoeud(self, valeur):
        if self is not None and valeur is not None:
            if self.valeur == valeur:
                return self;
            elif self.valeur > valeur and self.gauche is not None:
                return self.gauche.trouverNoeud(valeur);
            elif self.valeur < valeur and self.droite is not None:
                return self.droite.trouverNoeud(valeur);
        return None;

    def minValue(self):
        if self.gauche is None:
            return self.valeur;
        else:
            return self.gauche.minValue();

    def maxValue(self):
        if self.droite is None:
            return self.valeur;
        else:
            return self.droite.maxValue();

    def ajouterNoeud(self, valeur):
        if self is not None:
            if valeur < self.valeur:
                if self.gauche is None:
                    self.gauche = Noeud(valeur);
                    self.gauche.parent = self;
                else:
                    self.gauche.ajouterNoeud(valeur);


            elif valeur > self.valeur:
                if self.droite is None:
                    self.droite = Noeud(valeur);
                    self.droite.parent = self;
                else:
                    self.droite.ajouterNoeud(valeur);

            else:
                print("Node already exists");

    # Méthode pour supprimer un noeud
    def supprimerNoeud(self, valeur):
        if valeur is None:
            return;
        if valeur < self.valeur:
            if self.gauche is not None:
                return self.gauche.supprimerNoeud(valeur);
            else:
                return False;
        elif valeur > self.valeur:
            if self.droite is not None:
                return self.droite.supprimerNoeud(valeur);
            else:
                return False;
        else:
            if self.gauche is not None and self.droite is not None:
                valeurGauche = self.gauche.minValue();
                valeurDroite = self.droite.maxValue();

                if self.valeur - valeurGauche < valeurDroite - self.valeur:
                    self.gauche.supprimerNoeud(valeurGauche);
                    self.valeur = valeurGauche;
                else:
                    self.droite.supprimerNoeud(valeurDroite);
                    self.valeur = valeurDroite;


            elif self.parent.gauche == self:
                if self.gauche is not None:
                    self.parent.gauche = self.gauche;
                else:
                    self.parent.gauche = self.droite;
            elif self.parent.droite == self:
                if self.gauche is not None:
                    self.parent.droite = self.gauche;
                else:
                    self.parent.droite = self.droite;

            return True;

    # Méthode pour afficher l’arbre selon un parcours infixe
    # Cette méthode doit retournée un tableau contenant la valeur des noeuds
    def infixeNoeud(self, array):
        if self is not None:
            if self.gauche is not None:
                self.gauche.infixeNoeud(array);

            if self.valeur is not None:
                array.append(str(self.valeur));

            if self.droite is not None:
                self.droite.infixeNoeud(array);


class Arbre:
    def __init__(self):
        self.racine = None

    # Méthode pour trouver une valeur donnée dans un arbre binaire de recherche
    def trouverNoeud(self, val):
        if self.racine is None:
            return False;
        return self.racine.trouverNoeud(val);

    # Méthode pour ajouter un noeud
    def ajouterNoeud(self, val):
        if self.racine is None:
            self.racine = Noeud(val);
        else:
            self.racine.ajouterNoeud(val)

    # Méthode pour supprimer un noeud
    def supprimerNoeud(self, val):
        if self.racine.valeur == val:
            self.racine = None;
        else:
            self.racine.supprimerNoeud(val);

    # Méthode pour afficher l’arbre selon un parcours infixe
    # Cette méthode doit retournée un tableau contenant la valeur des noeuds
    def infixe(self):
        array = [];
        if self is not None:
            if self.racine is not None:
                self.racine.infixeNoeud(array);
                return array;

    # Méthode pour afficher la valeur d'un noeud à partir de sa valeur
    def printNoeud(self, val):
        noeud = self.trouverNoeud(val)
        if noeud is not None:
            noeud.toString()