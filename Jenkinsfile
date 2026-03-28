pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml_astronomico .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm ml_astronomico pytest tests/'
            }
        }

        stage('Run Main Script') {
            steps {
                sh 'mkdir -p outputs'
                sh 'docker rm -f ml_astronomico_run || true'
                sh 'docker run --name ml_astronomico_run ml_astronomico'
            }
        }

        stage('Copy Outputs From Container') {
            steps {
                sh 'docker cp ml_astronomico_run:/app/outputs/. outputs/'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }

    post {
        always {
            sh 'docker rm -f ml_astronomico_run || true'
        }
    }
}