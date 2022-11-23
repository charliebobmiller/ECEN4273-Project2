pipeline {
    any {
        docker { image 'qnib/pytest' }
    }

    stages {
        stage('Tests') {
            steps {
                sh  'pytest --junitxml build\\report.xml tests\\'
                junit 'build\\report.xml'
            }
        }
    }
}