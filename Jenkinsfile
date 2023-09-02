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
    }
}
