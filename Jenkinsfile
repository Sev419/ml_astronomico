pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run') {
            steps {
                sh 'python3 src/main.py'
            }
        }

        stage('Artifacts') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }
}