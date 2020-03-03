class Cercle {
    constructor(rayon) {
        this.rayon = rayon;
    }

    perimetre() {
        return 2 * Math.PI * this.rayon;
    }

    aire() {
        return Math.PI * Math.pow(this.rayon, 2);
    }

}