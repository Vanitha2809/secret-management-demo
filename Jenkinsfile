pipeline {
    agent any

    environment {
        DB_USER = credentials('db-user')
        DB_PASS = credentials('db-pass')
    }

    stages {
        stage('Run Python App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
