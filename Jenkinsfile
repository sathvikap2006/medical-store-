pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install Dependencies') {
            steps { bat 'python -m pip install -r requirements.txt' }
        }
        stage('Unit Tests') {
            steps { bat 'python -m pytest -v' }
        }
        stage('Build Docker Image') {
            steps { bat 'docker build -t sindhujha06/medical-store:v1 .' }
        }
    }
}
