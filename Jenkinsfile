pipeline {
    agent any

    stages {
        stage('Clear') {
            steps {
                script {
                    def runningContainers = sh(script: 'docker ps -aq', returnStdout: true).trim()
                    if (!runningContainers.isEmpty()) {
                        sh "docker stop ${runningContainers}"
                    }
                    
                }
                
                sh 'docker container prune -f'
                sh 'docker image prune -f'
            }
        }
        
        stage('Initialize') {
            steps {
                git branch: 'main', url: 'https://github.com/0xd4ydream/ci-cd-pipeline-flask-app.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                timeout(time: 30, unit: "MINUTES") {
                    input message: 'Do you want to deploy to production?', ok: 'Yes'
                }
                
                sh 'docker run -d -p 80:5000 --name=flask-app flask-app'
            }
        }
        
    }
}