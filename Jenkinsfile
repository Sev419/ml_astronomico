pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el proyecto'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml_astronomico .'
            }
        }

        stage('Run Tests and Main Script in Docker') {
            steps {
                sh 'mkdir -p outputs'
                sh 'docker run --rm -v $WORKSPACE/outputs:/app/outputs ml_astronomico'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }
}