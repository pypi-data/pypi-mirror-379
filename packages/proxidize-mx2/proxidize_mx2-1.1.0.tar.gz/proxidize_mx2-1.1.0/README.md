# Proxidize MX2 Manager - INTERNAL USE ONLY

**⚠️ CONFIDENTIAL - INTERNAL TEAM USE ONLY ⚠️**

This is proprietary Proxidize company software for internal team use only. This tool is NOT for public distribution or external sharing.

## Internal Tool Overvie## License & Usage

```
PROPRIETARY SOFTWARE - INTERNAL USE ONLY

Copyright (c) 2025 Proxidize Inc. All Rights Reserved.

This software is proprietary to Proxidize Inc. and is intended for internal
team use only. Unauthorized distribution, modification, or use outside of
Proxidize Inc. is strictly prohibited.

For internal team use only - Do not distribute externally.
```

**⚠️ CONFIDENTIAL: This tool contains proprietary Proxidize IP and trade secrets.**ize MX2 Manager is an internal command-line interface developed for Proxidize team members to handle large-scale deployments of Proxidize MX2 cellular modems. This internal tool provides enterprise-grade bulk operations with multi-threaded architecture capable of managing 40+ modems concurrently.

**For Proxidize team members only** - Contact your manager for access and usage guidelines.

## Key Features

### Bulk Operations

- **Concurrent Management**: Handle 40+ Proxidize MX2 modems simultaneously with optimized multi-threading (up to 120 workers)
- **Carrier Grouping**: Automatically organize modems by network carrier for streamlined operations
- **Progress Tracking**: Real-time progress indicators with completion statistics
- **Performance Optimized**: Intelligent caching and connection pooling for maximum efficiency

### Professional Interface

- **Brand Integration**: Clean interface with official Proxidize branding colors
- **Interactive Menus**: Intuitive navigation with clear confirmation prompts for safety
- **Dynamic Status**: Real-time displays showing connection counts and carrier information
- **Cross-Platform**: Consistent experience across Windows, Linux, and macOS

### Complete APN Management

- **Profile Creation**: Create custom APN profiles with username/password authentication
- **Bulk Configuration**: Apply APN settings across multiple Proxidize MX2 modems simultaneously
- **Profile Management**: List, view, delete, and set default APN profiles
- **Proper Workflow**: Implements disconnect-configure-reconnect sequence for reliable changes

### Network Operations

- **Connection Control**: Connect, disconnect, and soft restart modems with proper timing
- **Network Mode Selection**: Switch between Auto, 4G LTE Only, 3G Only, and 2G Only modes
- **Status Monitoring**: Real-time connection status with intelligent retry logic
- **Signal Analysis**: Comprehensive signal strength reporting (RSRP, RSRQ, SINR metrics)

### Advanced Monitoring

- **Status Dashboard**: Comprehensive modem status with detailed signal metrics
- **Public IP Detection**: Automatic public IP resolution for connectivity verification
- **CSV Export**: Professional data export for reporting and analysis
- **Smart Caching**: 5-minute cache system for improved performance in large deployments

### Enterprise Features

- **Multi-threaded Architecture**: Up to 120 concurrent workers for maximum throughput
- **Error Recovery**: Robust error handling with automatic retries and graceful degradation
- **Safety Controls**: Multiple confirmation prompts for destructive operations
- **Flexible Configuration**: Adaptable to different deployment scenarios and network conditions

## Installation (Internal Team Only)

### For Proxidize Team Members

This tool is available through internal channels only. Contact your team lead for proper installation instructions.

### Development Installation (Internal)

For internal development and modifications:

```bash
# Internal team repository access required
# Contact your manager for repository access
git clone [INTERNAL_REPO_URL]
cd proxidize-mx2-manager

# Install dependencies
pip install -r requirements.txt

# Run directly
python main.py
```

## Usage

### Starting the Application

After installation via pipx, start the manager:

```bash
proxidize_mx2
```

### Initial Setup

1. **Prepare Your Proxy List**: Gather HTTP proxy credentials for your Proxidize MX2 modems in the format:

   ```
   host:port:username:password
   ```

2. **Launch Application**: Run `proxidize_mx2` command

3. **Input Proxies**: Paste your proxy list (one per line) and press Enter on an empty line

4. **Wait for Probe**: The system will test connectivity to all modems

5. **Choose Operations**: Select from the interactive menu based on your needs

## Main Features Overview

### Bulk Operations Menu

Perfect for enterprise deployments with multiple Proxidize MX2 modems:

- **View All Modems Status**: Comprehensive status table with signal strength, connection state, and carrier info
- **Export Status to CSV**: Generate detailed reports including public IP addresses and signal metrics
- **Bulk Connect/Disconnect**: Manage connections across entire fleets with progress tracking
- **Bulk Soft Restart**: Refresh connections without full reboot for network troubleshooting
- **Bulk APN Management**: Configure APN settings across multiple devices simultaneously
- **Network Mode Configuration**: Switch network modes (4G/3G/2G) across carrier groups
- **Factory Reset Operations**: Mass factory reset with multiple safety confirmations

### Single Modem Operations

For targeted management of specific Proxidize MX2 devices:

- **Individual Status Check**: Detailed information for single modem including signal analysis
- **APN Profile Management**: Create, view, delete, and manage APN profiles per device
- **Connection Management**: Connect, disconnect, soft restart individual modems with timing control
- **Network Mode Selection**: Change network preferences per device (Auto/4G/3G/2G)
- **Device Management**: Restart or factory reset individual modems with confirmation prompts

### Carrier-Based Grouping

Automatically organizes Proxidize MX2 modems by detected carrier for efficient management:

- **Automatic Detection**: Groups modems by network carrier (Verizon, AT&T, T-Mobile, etc.)
- **Group Operations**: Apply changes to all modems on the same carrier network
- **Selective Management**: Choose specific carrier groups for targeted operations
- **Load Balancing**: Distribute operations across carriers for optimal performance

### CSV Export and Reporting

Comprehensive data export capabilities for enterprise reporting:

- **Status Reports**: Export complete modem status including signal strength and connection details
- **Public IP Mapping**: Automatic public IP detection and export for network analysis
- **Signal Metrics**: RSRP, RSRQ, and SINR measurements for network quality assessment
- **Carrier Distribution**: Analysis of modem distribution across different carrier networks

## Technical Implementation

### Architecture

- **Multi-threaded Design**: Concurrent operations with configurable worker pools (up to 120 workers)
- **Modular Structure**: Clean separation of concerns across specialized modules
- **Error Resilience**: Comprehensive error handling with automatic retries and graceful degradation
- **Cross-Platform**: Native support for Windows, Linux, and macOS with proper path handling

### Network Operations

- **Proper API Workflow**: Implements disconnect → configure → connect sequence for reliable configuration changes
- **Connection Pooling**: Efficient HTTP connection management for improved performance
- **Timeout Management**: Smart timeout handling with exponential backoff for unreliable connections
- **Fallback Mechanisms**: Multiple API endpoints with automatic fallback for maximum compatibility

### Performance Optimization

- **Intelligent Caching**: 5-minute cache validity for bulk status operations
- **Progress Tracking**: Real-time progress indicators with completion statistics
- **Memory Management**: Efficient handling of large Proxidize MX2 modem deployments
- **Quiet Mode**: Streamlined output for automated operations

### Security and Reliability

- **Secure Communication**: HTTP-based API with proper authentication handling
- **Input Validation**: Comprehensive validation of proxy formats and user inputs
- **Safety Controls**: Multiple confirmation prompts for destructive operations
- **Graceful Shutdown**: Proper cleanup on interruption or termination

## Requirements

- **Python**: 3.8 or higher
- **Network Access**: HTTP connectivity to Proxidize MX2 modem proxy endpoints
- **Compatible Modems**: Proxidize MX2 family modems with HTTP API enabled
- **Operating System**: Windows 10+, Linux (Ubuntu/CentOS/Debian), macOS 10.14+

## Troubleshooting

### Common Issues

**Connection Problems:**

```bash
# Check proxy format
host:port:username:password

# Test individual connection
curl -x http://username:password@host:port http://httpbin.org/ip
```

**Installation Issues:**

```bash
# Ensure pipx is properly installed
python -m pip install --user pipx
pipx ensurepath

# Reinstall if needed
pipx uninstall proxidize_mx2
pipx install proxidize_mx2
```

**Performance Optimization:**

- Reduce worker count for slower networks
- Use carrier grouping for better organization
- Enable caching for repeated operations

## Use Cases

### Enterprise IT Teams

- **Large Deployments**: Manage 40+ Proxidize MX2 modems across multiple locations
- **Configuration Management**: Standardize APN and network settings across deployments
- **Status Monitoring**: Regular health checks and performance monitoring
- **Troubleshooting**: Quick diagnosis and resolution of connectivity issues

### Network Operations Centers

- **Bulk Operations**: Efficient mass configuration changes across Proxidize MX2 fleets
- **Carrier Management**: Organize and manage multi-carrier deployments
- **Performance Analysis**: Export data for network performance analysis
- **Automated Workflows**: Integration with existing monitoring systems

### Field Technicians

- **Quick Setup**: Rapid deployment and configuration of new Proxidize MX2 modems
- **Diagnostics**: Comprehensive status checking and signal analysis
- **Remote Management**: Manage modems without physical access
- **Documentation**: CSV exports for installation records

## About This Internal Tool

**Proxidize MX2 Manager** was developed by Fawaz Al-Ghzawi for internal Proxidize team use to address operational challenges in managing large Proxidize MX2 cellular modem deployments. This internal tool is proprietary Proxidize IP.

### Internal Support

- **Developer**: Fawaz Al-Ghzawi (Internal Team)
- **Internal Contact**: Use internal Proxidize communication channels
- **Repository**: Private internal repository (team access only)
- **Support**: Internal team support only

### Proxidize Company Resources

- **Internal Wiki**: [Internal documentation access required]
- **Official Website**: [https://proxidize.com](https://proxidize.com)

### Internal Support Channels

- **Internal Issues**: Use internal ticketing system
- **Feature Requests**: Internal team discussions only
- **Documentation**: This README and internal documentation
- **Support**: Internal team support through company channels

## 📄 **License**

```
MIT License

Copyright (c) 2025 Fawaz Al-Ghzawi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

**Full license text available in [LICENSE](LICENSE) file.**
