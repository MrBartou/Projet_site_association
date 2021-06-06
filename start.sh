#!/usr/bin/env bash

echo -e "\n              0000_____________0000________0000000000000000__000000000000000000+\n            00000000_________00000000______000000000000000__0000000000000000000+\n           000____000_______000____000_____000_______0000__00______0+\n          000______000_____000______000_____________0000___00______0+\n         0000______0000___0000______0000___________0000_____0_____0+\n         0000______0000___0000______0000__________0000___________0+\n         0000______0000___0000______0000_________000___0000000000+\n         0000______0000___0000______0000________0000+\n          000______000_____000______000________0000+\n           000____000_______000____000_______00000+\n            00000000_________00000000_______0000000+\n              0000_____________0000________000000007;"

tput setaf 1
echo -e "\nBienvenue sur le gestionnaire de lancement du Site pour les Association\n\n"
tput sgr0

function all {
        echo -e "\nLancement du Docker compose\n"
        docker-compose up
        echo -e "\nfermeture du Container, pensez a supprimer celui-ci\n"
        echo -e "\nScript by MrBartou for Project Hub Epitech TOULOUSE"
        exit 0
}

function frontend {
        echo -e "\nentrée dans ./frontend\n"
        cd frontend
        echo -e "\nLancement du Docker compose\n"
        docker-compose up
        echo -e "\nfermeture du Container, pensez a supprimer celui-ci\n"
        echo -e "\nScript by MrBartou for Project Hub Epitech TOULOUSE"
        exit 0
}

function backend {
        echo -e "\nentrée dans ./backend\n"
        cd backend
        echo -e "\nLancement du Docker compose\n"
        docker-compose up
        echo -e "\nfermeture du Container, pensez a supprimer celui-ci\n"
        echo -e "\nScript by MrBartou for Project Hub Epitech TOULOUSE"
        exit 0
}

function documentation {
        echo -e "\nentrée dans ./backend\n"
        cd backend
        echo -e "\nGénération de la documentation\n"
        pdoc --html backend/backend
        echo -e "\nScript by MrBartou for Project Hub Epitech TOULOUSE"
        exit 0
}

function nettoyage {
        echo -e "\nnettoyage de docker en cours\n"
        docker-compose rm
        sleep 1
        docker image rm backend_web
        sleep 1
        docker image rm frontend_frontend
        sleep 1
        docker image rm projet_site_association_backend
        sleep 1
        docker image rm projet_site_association_frontend
        sleep 1
        docker container rm frontend_frontend_1
        sleep 1
        docker container rm backend_web_1
        sleep 1
        docker container rm projet_site_association_backend
        sleep 1
        docker container rm projet_site_association_frontend
        echo -e "\nScript by MrBartou for Project Hub Epitech TOULOUSE"
        exit 0
}

PS3="Que voulez vous lancer : "

select item in "- Tout -" "- Backend -" "- Frontend -" "- Documentation -" "- Nettoyage -" "- Quit -"
do
    for var in $REPLY; do
        echo -e "\nVous avez choisi l'item $var : $item \n"
        case $var in
                1)
                        all
                        ;;
                2)
                        backend
                        ;;
                3)
                        frontend
                        ;;
                4)
                        documentation
                        ;;
                5)
                        nettoyage
                        ;;
                6)
                        echo "Fin du script"
                        exit 0
                        ;;
                *)
                        echo "Choix incorrect"
                        ;;
        esac
    done
done