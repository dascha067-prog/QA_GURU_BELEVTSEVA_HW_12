pipeline {
    agent any

    stages {
        stage('Install deps') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Publish Allure') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
