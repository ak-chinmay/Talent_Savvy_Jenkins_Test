pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        PYTHON_VERSION = '3.8'  // Define the Python version
        VENV_DIR = 'venv'  // Virtual environment directory
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    echo 'Creating virtual environment...'
                    sh 'python3 -m venv ${VENV_DIR}'
                    sh '. ${VENV_DIR}/bin/activate && pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing project dependencies using setup.py...'
                    sh '. ${VENV_DIR}/bin/activate && pip install . && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running unit tests...'
                    sh '. ${VENV_DIR}/bin/activate &&  pytest --junitxml="test-report.xml"'
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                echo 'Archiving test results...'
                junit 'test-report.xml'  // If using JUnit-style test reports
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment...'
            sh 'rm -rf ${VENV_DIR}'
        }
        success {
            echo 'Build and tests passed successfully!'
        }
        failure {
            echo 'Build or tests failed.'
        }
    }
}
