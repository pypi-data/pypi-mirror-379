# Pulumi Runner Provider

An alternative way to run scripts locally and remotely for Pulumi infrastructure management.

## Overview

The Pulumi Runner provider enables you to execute commands and deploy files to remote servers via SSH as part of your Pulumi infrastructure workflows. This provider is particularly useful for:

- Deploying applications to remote servers
- Running configuration scripts on target machines
- Managing file assets and their deployment
- Executing custom operations during infrastructure lifecycle events

## Features

- **SSH Deployer Resource**: Execute commands on remote servers via SSH
- **File Asset Management**: Upload local files or create files from string content
- **Lifecycle Operations**: Define different commands for create, update, and delete operations
- **Multi-language Support**: Available for Go, Node.js, Python, and .NET
- **Preview Mode**: Preview operations before execution

## Installation

### Node.js/TypeScript

```bash
npm install @svmkit/pulumi-runner
```

### Python

```bash
pip install pulumi_runner
```

### Go

```bash
go get github.com/abklabs/pulumi-runner/sdk/go
```

### .NET

```bash
dotnet add package ABKLabs.Runner
```

## Quick Start

### Node.js/TypeScript Example

```typescript
import * as runner from "@svmkit/pulumi-runner";
import * as pulumi from "@pulumi/pulumi";

// Create an SSH deployer
const deployer = new runner.SSHDeployer("my-deployer", {
    connection: {
        host: "example.com",
        user: "ubuntu",
        privateKey: "-----BEGIN PRIVATE KEY-----\n...",
    },
    payload: [
        {
            localPath: "./app.tar.gz",
            mode: 0o644,
        },
        {
            contents: "#!/bin/bash\necho 'Hello World'",
            filename: "hello.sh",
            mode: 0o755,
        }
    ],
    create: {
        command: "tar -xzf app.tar.gz && ./deploy.sh",
        environment: {
            NODE_ENV: "production",
        },
    },
    update: {
        command: "tar -xzf app.tar.gz && ./update.sh",
        environment: {
            NODE_ENV: "production",
        },
    },
    delete: {
        command: "./cleanup.sh",
        environment: {
            CLEANUP_MODE: "force",
        },
    },
});
```

### Python Example

```python
import pulumi
import pulumi_runner as runner

# Create an SSH deployer
deployer = runner.SSHDeployer("my-deployer",
    connection=runner.ConnectionArgs(
        host="example.com",
        user="ubuntu",
        private_key="-----BEGIN PRIVATE KEY-----\n...",
    ),
    payload=[
        runner.FileAssetArgs(
            local_path="./app.tar.gz",
            mode=0o644,
        ),
        runner.FileAssetArgs(
            contents="#!/bin/bash\necho 'Hello World'",
            filename="hello.sh",
            mode=0o755,
        )
    ],
    create=runner.CommandDefinitionArgs(
        command="tar -xzf app.tar.gz && ./deploy.sh",
        environment={
            "NODE_ENV": "production",
        },
    ),
    update=runner.CommandDefinitionArgs(
        command="tar -xzf app.tar.gz && ./update.sh",
        environment={
            "NODE_ENV": "production",
        },
    ),
    delete=runner.CommandDefinitionArgs(
        command="./cleanup.sh",
        environment={
            "CLEANUP_MODE": "force",
        },
    ),
)
```

## Resources

### SSHDeployer

The main resource for executing commands on remote servers via SSH.

#### Properties

- **connection** (required): SSH connection configuration
  - `host`: Target server hostname or IP
  - `user`: SSH username
  - `privateKey`: SSH private key content
  - `port`: SSH port (optional, defaults to 22)
  - `proxy`: Proxy connection configuration (optional)

- **payload** (optional): Array of files to upload
  - `localPath`: Path to local file to upload
  - `contents`: File content as string
  - `filename`: Filename when using contents
  - `mode`: File permissions (e.g., 0o755)

- **environment** (optional): Global environment variables for all operations
  - Key-value pairs of environment variables

- **create** (optional): CommandDefinition for resource creation
- **update** (optional): CommandDefinition for resource updates  
- **delete** (optional): CommandDefinition for resource deletion

#### CommandDefinition Properties

Each operation (create, update, delete) is a CommandDefinition object with:
- **command** (required): Shell command to execute on the remote server
- **payload** (optional): Additional files to upload for this specific operation
- **environment** (optional): Environment variables specific to this operation

The command is executed in the context of the uploaded files and
environment variables, allowing you to reference them in your scripts
(e.g., `./deploy.sh`, `tar -xzf app.tar.gz`, `echo $NODE_ENV`).

**Note**: Global `payload` and `environment` settings are merged with
operation-specific settings, with operation-specific values taking precedence.

## Functions

### LocalFile

Creates a file asset from a local file path.

```typescript
const fileAsset = runner.LocalFile({
    localPath: "./config.json",
    mode: 0o644,
});
```

### StringFile

Creates a file asset from string content.

```typescript
const fileAsset = runner.StringFile({
    contents: '{"key": "value"}',
    filename: "config.json",
    mode: 0o644,
});
```

## Connection Configuration

### Basic SSH Connection

```typescript
const connection = {
    host: "192.168.1.100",
    user: "ubuntu",
    privateKey: "-----BEGIN PRIVATE KEY-----\n...",
    port: 22,
};
```

### SSH Connection with Proxy

```typescript
const connection = {
    host: "target-server.com",
    user: "admin",
    privateKey: "-----BEGIN PRIVATE KEY-----\n...",
    proxy: {
        host: "bastion.example.com",
        user: "bastion-user",
        privateKey: "-----BEGIN PRIVATE KEY-----\n...",
    },
};
```

## File Assets

File assets can be created in two ways:

### From Local Files

```typescript
{
    localPath: "./path/to/local/file",
    mode: 0o644,
}
```

### From String Content

```typescript
{
    contents: "file content here",
    filename: "remote-filename.txt",
    mode: 0o755,
}
```

## Best Practices

1. **Use preview mode**: Always test your deployments with `pulumi preview` first
2. **Idempotent commands**: Ensure your commands can be run multiple times safely
3. **Error handling**: Include proper error handling in your deployment scripts
4. **File permissions**: Set appropriate file permissions for uploaded files
5. **SSH keys**: Use SSH key authentication instead of passwords for security

## Development

### Building the Provider

```bash
make build
```

### Running Tests

```bash
make test
```

### Linting

```bash
make lint
```

## License

This project is licensed under the GNU Lesser General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For support and questions, please open an issue on the [GitHub repository](https://github.com/abklabs/pulumi-runner).

## Publisher

Published by [ABK Labs](https://abklabs.com)