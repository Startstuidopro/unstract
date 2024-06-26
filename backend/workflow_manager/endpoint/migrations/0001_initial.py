# Generated by Django 4.2.1 on 2024-01-23 11:18

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("connector", "0001_initial"),
        ("workflow", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowEndpoint",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "endpoint_type",
                    models.CharField(
                        choices=[
                            ("SOURCE", "Source connector"),
                            ("DESTINATION", "Destination Connector"),
                        ],
                        db_comment="Endpoint type (source or destination)",
                        editable=False,
                    ),
                ),
                (
                    "connection_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("FILESYSTEM", "FileSystem connector"),
                            ("DATABASE", "Database Connector"),
                            ("API", "API Connector"),
                        ],
                        db_comment="Connection type (Filesystem, Database or API)",
                    ),
                ),
                (
                    "configuration",
                    models.JSONField(
                        blank=True,
                        db_comment="Configuration in JSON format",
                        null=True,
                    ),
                ),
                (
                    "connector_instance",
                    models.ForeignKey(
                        db_comment="Foreign key from ConnectorInstance model",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="connector.connectorinstance",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        db_comment="Foreign key from Workflow model",
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workflow.workflow",
                    ),
                ),
            ],
            options={
                "verbose_name": "Workflow Endpoint",
                "verbose_name_plural": "Workflow Endpoints",
                "db_table": "workflow_endpoints",
            },
        ),
    ]
