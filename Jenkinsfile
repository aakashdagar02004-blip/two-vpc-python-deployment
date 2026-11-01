pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Ansible') {
            steps {
                sh 'ansible-playbook --syntax-check -i ansible/inventory.ini ansible/deploy-python-app.yml'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy-python-app.yml'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl --fail --silent --show-error http://10.0.1.13/health'
            }
        }
    }
}
