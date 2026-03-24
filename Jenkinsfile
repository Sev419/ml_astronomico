pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Run') {
            steps {
                bat 'python src/main.py'
            }
        }

        stage('Artifacts') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }
}