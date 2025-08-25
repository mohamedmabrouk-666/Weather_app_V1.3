pipeline {
    agent any

    stages {


          stage('Checkout') {
            steps {
                    git branch: 'main',
                    url: 'git@github.com:mohamedmabrouk-666/Weather_app_V1.3.git',
                    credentialsId: 'weather-app-on-Git'
            }
        }


           stage('Lint Test') {
            steps {
                 sh '''
                    flake8 /app/main.py
                    flake8 /app/weather.py
                '''

                  }
                     }


           stage('Build Docker image from Dockerfile') {
            steps {
                 sh 'docker rmi -f app/my-app || true' // To delete any image using same image
                 sh 'docker build -t app/my-app ./app'
                 }
                  }     


         stage('Run Docker image by name my-app') {
            steps {
                 sh 'docker rm -f my_app || true' // To delete any container using same name
                 sh 'docker run --name my_app app/my-app'
            }
    }    
    
         
   
        stage('Unit Test') {
             steps {
               sh '''
                    pytest tests/test_app.py
                    pytest tests/test_cli_app.py
                '''
                   }
                           }

        
    }

    post {
        success {
            echo 'Build successful'
        }
        failure {
            echo 'Build failed'
        }
        always {
            echo 'Pipeline is completed'
        }
    }

}