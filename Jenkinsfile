pipeline {
    agent any  // Runs on any available Jenkins agent
    parameters {
            choice(
                name: 'ENVIRONMENT',
                choices: ['dev', 'test', 'prod'],
                description: 'Select the deployment environment'
            )
            password(name: 'azure_passwd', defaultValue: '', description: 'azure password')
        }
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
                    sh 'echo "rootroot" | sudo -S apt install python3'
                    sh 'echo "rootroot" | sudo -S apt install python3-pip' 
                    sh 'pip install --upgrade pip'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Installing project    dependencies using setup.py...'
                    sh '. pip install . && pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running unit tests...'
                    sh '. pytest --junitxml="test-report.xml"'
                }

            }
        }

        stage('Deploy') {
            steps {
                script {
                        // Environment-specific deployment logic
                        switch(params.ENVIRONMENT) {
                            case 'dev':
                                echo "Deploying to Development"
                                // Add dev deployment steps
                                break
                            case 'test':
                                echo "Deploying to Test"
                                // Add test deployment steps
                                break
                            case 'prod':
                                echo "Deploying to Production"
                                // Add production deployment steps with additional approvals
                                input message: 'Deploy to production?'
                                break
                        }
                }
            }
        }

        stage('Deploy 2') {
            steps {
                script {
                        // Environment-specific deployment logic
                        switch(params.ENVIRONMENT) {
                            case 'dev':
                                echo "Deploying to Development"
                                // Add dev deployment steps
                                break
                            case 'test':
                                echo "Deploying to Test"
                                // Add test deployment steps
                                break
                            case 'prod':
                                echo "Deploying to Production"
                                // Add production deployment steps with additional approvals
                                input message: 'Deploy to production?'
                                break
                        }
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
