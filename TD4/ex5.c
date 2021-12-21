#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_ROW 5

int random_bit()
{
    float nombre = 0;

    nombre = rand() / (RAND_MAX + 1.0);
    if (nombre > 0.5)
        return 1;
    else
        return 0;
}

void free_matrice(int **matrice)
{
    for (int i = 0; i < NB_ROW; i++)
    {
        free(matrice[i]);
    }
    free(matrice);
}

int **creer_matrice()
{
    int **matrice;
    matrice = malloc(NB_ROW * sizeof(*matrice));
    for (int i = 0; i < NB_ROW; i++)
    {
        matrice[i] = malloc(NB_ROW * sizeof(**matrice));
    }
    return matrice;
}

void init_matrice(int **matrice)
{
    for (int i = 0; i < NB_ROW; i++)
    {
        for (int j = 0; j < NB_ROW; j++)
        {
            matrice[i][j] = random_bit();
        }
    }
}

void afficher_matrice(int **matrice)
{
    for (int i = 0; i < NB_ROW; i++)
    {
        for (int j = 0; j < NB_ROW; j++)
        {
            printf("%d  ", matrice[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int nombre_voisins(int **matrice, int x, int y)
{
    int nb;
    nb = matrice[(x - 1 + NB_ROW) % NB_ROW][(y - 1 + NB_ROW) % NB_ROW] + matrice[(x - 1 + NB_ROW) % NB_ROW][(y + NB_ROW) % NB_ROW] +
         matrice[(x - 1 + NB_ROW) % NB_ROW][(y + 1 + NB_ROW) % NB_ROW] + matrice[(x + NB_ROW) % NB_ROW][(y + 1 + NB_ROW) % NB_ROW] +
         matrice[(x + 1 + NB_ROW) % NB_ROW][(y + 1 + NB_ROW) % NB_ROW] + matrice[(x + 1 + NB_ROW) % NB_ROW][(y + NB_ROW) % NB_ROW] +
         matrice[(x + 1 + NB_ROW) % NB_ROW][(y - 1 + NB_ROW) % NB_ROW] + matrice[(x + NB_ROW) % NB_ROW][(y - 1 + NB_ROW) % NB_ROW];
    return nb;
}

int **apply_generation(int **matrice)
{
    int **new_matrice = creer_matrice();
    for (int i = 0; i < NB_ROW; i++)
    {
        for (int j = 0; j < NB_ROW; j++)
        {
            if (matrice[i][j])
            {
                if (nombre_voisins(matrice, i, j) >= 4)
                {
                    new_matrice[i][j] = 0;
                }
                else if (nombre_voisins(matrice, i, j) <= 1)
                {
                    new_matrice[i][j] = 0;
                }
                else
                    new_matrice[i][j] = 1;
            }
            else
            {
                if (nombre_voisins(matrice, i, j) == 3)
                {
                    new_matrice[i][j] = 1;
                }
                else
                    new_matrice[i][j] = 0;
            }
        }
    }
    free_matrice(matrice);
    return new_matrice;
}

int main()
{
    srand(time(NULL));
    int **matrice = creer_matrice();
    init_matrice(matrice);
    int nb_generations;
    printf("Combien voulez vous de generations ? \n");
    scanf("%d", &nb_generations);
    printf("Premiere generation : \n");
    afficher_matrice(matrice);
    for (int i = 0; i < nb_generations - 1; i++)
    {
        matrice = apply_generation(matrice);
        printf("Generation numero %d : \n", i + 2);
        afficher_matrice(matrice);
    }
    free_matrice(matrice);
}