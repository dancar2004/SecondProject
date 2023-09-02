pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }

    stages {
        stage("test") {
            steps {
                echo 'Hellow World'                
            }
        }

        stage("checkout"){
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git 'https://github.com/dancar2004/SecondProject.git'
            }
        }

        stage("run backend server"){
            steps {
                script {
                    bat 'start/min python rest_app.py'
                }
            }
        }

        stage("run frontend server"){
            steps {
                script {
                    bat 'start/min python web_app.py'
                }
            }
        }
    }
}