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
                scripts {
                    properties([pipelineTriggers([pollSCM('H/30 * * * * *')])])
                }
                git 'https://github.com/dancar2004/SecondProject.git'
            }
        }

        stage("build"){
            steps {
                echo 'Completed Successfully'
            }
        }
    }
}
