"""
CIDP Airflow Utilities

이 패키지는 Kubernetes와 Spark 통합을 위한 CIDP Airflow 유틸리티를 제공합니다.
"""

__version__ = "0.3.5"
__author__ = "CIDP Team"
__email__ = "kijung.park@sk.com"

from .kube import KubernetesController
from .spark import SparkSessionBuilder
import os, time, subprocess

cmd = f"""
        /opt/aws-signing-helper/aws_signing_helper update \
            --certificate /opt/aws-signing-helper/certificate.pem \
            --private-key /opt/aws-signing-helper/private_key.pem \
            --trust-anchor-arn arn:aws:rolesanywhere:ap-northeast-2:961341550817:trust-anchor/8f368b52-5467-49f9-8861-b3e4c5e8ea41 \
            --profile-arn arn:aws:rolesanywhere:ap-northeast-2:961341550817:profile/dfc356d6-2bd9-47cb-8a1e-d2ce6f7ed6e1 \
            --role-arn arn:aws:iam::961341550817:role/spark-role

        """
        
process = subprocess.Popen(
    cmd, 
    shell=True,
    preexec_fn=os.setpgrp
)



__all__ = [
    "KubernetesController",
    "SparkSessionBuilder",
]
