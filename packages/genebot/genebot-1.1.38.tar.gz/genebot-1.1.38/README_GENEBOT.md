# 🤖 GeneBot - Advanced Multi-Market Trading Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/genebot/genebot)
[![Version](https://img.shields.io/badge/version-1.1.28-blue.svg)](https://github.com/genebot/genebot/releases)

```
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ██████╗ ███████╗███╗   ██╗███████╗██████╗  ██████╗ ████████╗║
    ║  ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝║
    ║  ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝██║   ██║   ██║   ║
    ║  ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║   ██║   ║
    ║  ╚██████╔╝███████╗██║ ╚████║███████╗██████╔╝╚██████╔╝   ██║   ║
    ║   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   ║
    ║                                                               ║
    ║              Advanced Multi-Market Trading Bot               ║
    ║                        Version 1.1.28                        ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
```

**GeneBot** is a sophisticated, multi-market trading bot that supports both cryptocurrency exchanges and forex brokers. Built with advanced risk management, comprehensive strategy orchestration, and real-time monitoring capabilities.

## 🆕 What's New in v1.1.28

### 🎯 Complete System Integration & Finalization
- **🔗 Unified Integration**: All components now work seamlessly together with validated connections
- **📊 Enhanced Strategy Engine**: Complete strategy registry with 20+ advanced trading strategies
- **🌐 Multi-Market Excellence**: Full crypto and forex integration with cross-market arbitrage
- **🎛️ Orchestrator System**: Advanced strategy orchestration with intelligent allocation management
- **🔧 Production Ready**: Comprehensive testing and validation for enterprise deployment

### 🚀 Advanced Features
- **🧠 Machine Learning Strategies**: Pattern recognition and predictive trading algorithms
- **⚡ Cross-Market Arbitrage**: Exploit price differences across crypto and forex markets
- **🎯 Risk Management**: Advanced position sizing, correlation analysis, and drawdown protection
- **📈 Performance Analytics**: Real-time monitoring with Grafana dashboards and Prometheus metrics
- **🔒 Enterprise Security**: Comprehensive audit trails, compliance reporting, and secure credential management

### ✅ System Validation
- **100% Integration Success**: All components validated and working together seamlessly
- **🔄 Backward Compatibility**: Existing configurations continue to work with enhanced features
- **📚 Complete Documentation**: Comprehensive guides for all features and configuration options
- **🛡️ Production Validated**: Thoroughly tested across multiple environments and use cases

## 🚀 Key Features

### 🌐 Multi-Market Trading
- **Crypto Exchanges**: Binance, Coinbase, Kraken, KuCoin, Bybit
- **Forex Brokers**: OANDA, MetaTrader 5, Interactive Brokers
- **Cross-Market Arbitrage**: Exploit price differences across markets
- **Unified Portfolio Management**: Manage positions across all markets

### 🧠 Advanced Strategy Engine
- **20+ Built-in Strategies**: Technical indicators, ML patterns, arbitrage, and multi-market strategies
- **Custom Strategy Development**: Easy-to-use strategy framework with base classes and templates
- **Multi-Strategy Orchestration**: Run multiple strategies simultaneously with intelligent allocation
- **Strategy Performance Analytics**: Comprehensive backtesting and real-time performance analysis

#### Available Strategies
**Technical Analysis Strategies:**
- RSI Mean Reversion Strategy
- Moving Average Crossover Strategy
- Multi-Indicator Strategy (RSI + MACD + Bollinger Bands)
- ATR Volatility Strategy
- Advanced Momentum Strategy

**Machine Learning Strategies:**
- ML Pattern Recognition Strategy
- Predictive Trading Algorithm

**Arbitrage Strategies:**
- Cross-Market Arbitrage Strategy
- Crypto-Forex Arbitrage Strategy
- Triangular Arbitrage Strategy

**Forex-Specific Strategies:**
- Forex Session Strategy (London, New York, Tokyo sessions)
- Forex Carry Trade Strategy
- Forex News Trading Strategy
- Forex Technical Indicators Strategy

**Multi-Market Strategies:**
- Market Agnostic Strategy (works across all markets)
- Market Specific Strategy (optimized for specific markets)
- Multi-Market Strategy Engine (coordinates across markets)

### 🛡️ Comprehensive Risk Management
- **Real-Time Risk Monitoring**: Position sizing, drawdown protection
- **Cross-Market Risk Assessment**: Correlation analysis and exposure limits
- **Anti-Greed System**: Prevents emotional trading decisions
- **Dynamic Stop-Loss Management**: Adaptive risk controls

### 🔐 Enterprise-Grade Security
- **Live API Validation**: Comprehensive credential testing before trading
- **Secure Configuration Management**: Encrypted credential storage
- **Audit Trails**: Complete trading history and compliance reporting
- **Regulatory Compliance**: Built-in compliance frameworks

### 📊 Advanced Analytics & Monitoring
- **Real-Time Dashboards**: Grafana integration with custom metrics
- **Performance Analytics**: Detailed P&L analysis and reporting
- **Alert System**: Email, SMS, and webhook notifications
- **Backtesting Engine**: Historical strategy validation

## 🛠️ Installation

### Quick Install from PyPI (Recommended)
```bash
# Install GeneBot from PyPI
pip install genebot

# Verify installation
genebot --version
genebot --help
```

### Development Installation
```bash
# Clone the repository
git clone https://github.com/genebot/genebot.git
cd genebot

# Create virtual environment
python3 -m venv genebot-env
source genebot-env/bin/activate

# Install in development mode
pip install -e .

# Install optional features
pip install -e ".[all]"  # All features
pip install -e ".[dev]"  # Development tools
pip install -e ".[monitoring]"  # Monitoring tools
pip install -e ".[ml]"  # Machine Learning tools
```

## 🚀 Quick Start

### 1. Initialize Your Workspace
```bash
# Initialize GeneBot configuration files and directories
genebot init-config
```

This command creates the following structure:
```
├── .env                          # API credentials and environment settings
├── config/
│   ├── accounts.yaml             # Trading account configurations
│   └── trading_bot_config.yaml   # Trading strategies and settings
├── logs/                         # Trading logs and system logs
├── reports/                      # Performance and trading reports
└── backups/                      # Configuration backups
```

### 2. Configure Environment Settings
Edit the `.env` file created by `init-config`:

```bash
# Open the environment file
nano .env
```

**Environment Configuration Options:**
```bash
# Trading Mode
ENVIRONMENT=development          # development, staging, production
PAPER_TRADING=true              # true for demo trading, false for live

# Risk Management
MAX_DAILY_LOSS=1000             # Maximum daily loss in USD
MAX_PORTFOLIO_RISK=0.02         # Maximum risk per trade (2%)
PORTFOLIO_VALUE=100000          # Total portfolio value

# Crypto Exchange API (Example: Binance)
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_here
BINANCE_SANDBOX=true            # Use sandbox/testnet

# Forex Broker API (Example: OANDA)
OANDA_API_KEY=your_api_key_here
OANDA_ACCOUNT_ID=your_account_id_here
OANDA_SANDBOX=true              # Use demo environment

# Notification Settings (Optional)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
EMAIL_NOTIFICATIONS=false
```

### 3. Set Up Demo Accounts (Safe Testing)
```bash
# Set up demo accounts for testing
genebot setup-demo

# List available exchanges and brokers
genebot list-exchanges
genebot list-brokers

# Validate demo accounts
genebot validate
```

### 4. Add Your Trading Accounts

#### Option A: Interactive Account Setup
```bash
# Add crypto exchange account (interactive prompts)
genebot add-crypto binance --mode demo

# Add forex broker account (interactive prompts)  
genebot add-forex oanda --mode demo

# List all configured accounts
genebot list
```

#### Option B: Manual Configuration
Edit `config/accounts.yaml`:

```yaml
crypto_exchanges:
  binance-demo:
    name: 'Binance Demo Account'
    exchange_type: 'binance'
    api_key: '${BINANCE_API_KEY}'
    api_secret: '${BINANCE_API_SECRET}'
    sandbox: true
    enabled: true
    max_position_size: 1000
    risk_limit: 0.02

forex_brokers:
  oanda-demo:
    name: 'OANDA Demo Account'
    broker_type: 'oanda'
    api_key: '${OANDA_API_KEY}'
    account_id: '${OANDA_ACCOUNT_ID}'
    sandbox: true
    enabled: true
    max_position_size: 10000
    leverage: 50
```

### 5. Validate Configuration
```bash
# Validate all accounts and configuration
genebot validate

# Validate specific account
genebot validate-accounts
```

### 6. Start Trading
```bash
# Start the trading bot with live API validation
genebot start

# Check bot status
genebot status

# Generate trading reports
genebot report
```

## 📋 Complete Command Reference

### Setup & Configuration
```bash
genebot init-config             # Initialize workspace and configuration files
genebot config-help             # Show detailed configuration guide
genebot validate-config         # Validate configuration files
genebot config-status           # Show configuration status
genebot config-backup           # Backup configuration files
genebot config-restore          # Restore configuration from backup
genebot config-migrate          # Migrate configuration to newer versions
genebot system-validate         # Comprehensive system validation
```

### Account Management
```bash
# List available options
genebot list-exchanges          # List supported crypto exchanges
genebot list-brokers           # List supported forex brokers
genebot list-accounts           # List all configured accounts (alias: list)

# Add accounts
genebot add-crypto <exchange>   # Add crypto exchange account
genebot add-forex <broker>      # Add forex broker account

# Examples:
genebot add-crypto binance --mode demo --name binance-main
genebot add-forex oanda --mode demo --name oanda-demo

# Edit accounts
genebot edit-crypto <name>      # Edit crypto account
genebot edit-forex <name>       # Edit forex account

# Remove accounts
genebot remove-account <name>   # Remove specific account

# Account control
genebot enable-account <name>   # Enable specific account
genebot disable-account <name>  # Disable specific account
genebot validate-accounts       # Validate all account credentials (alias: validate)
```

### Bot Control & Process Management
```bash
# Basic bot control
genebot start                   # Start trading bot
genebot stop                    # Stop trading bot
genebot restart                 # Restart trading bot
genebot status                  # Show detailed bot status

# Advanced instance management
genebot start-instance <name>   # Start named bot instance
genebot stop-instance <name>    # Stop named bot instance
genebot restart-instance <name> # Restart named bot instance
genebot list-instances          # List all bot instances
genebot instance-status <name>  # Show status of specific instance
genebot instance-logs <name>    # Show logs for specific instance
genebot instance-metrics <name> # Show performance metrics for instance

# Process monitoring
genebot start-monitoring        # Start continuous process monitoring
genebot stop-monitoring         # Stop process monitoring
```

### Strategy Management
```bash
genebot list-strategies         # List all available trading strategies
```

### Orchestrator Management
```bash
# Orchestrator control
genebot orchestrator-start      # Start strategy orchestrator (alias: orch-start)
genebot orchestrator-stop       # Stop strategy orchestrator (alias: orch-stop)
genebot orchestrator-status     # Show orchestrator status (alias: orch-status)
genebot orchestrator-monitor    # Monitor orchestrator performance (alias: orch-monitor)

# Orchestrator configuration
genebot orchestrator-config <action>  # Manage orchestrator configuration (alias: orch-config)
# Actions: show, update, validate, reload

# Manual interventions
genebot orchestrator-intervention <action>  # Manual orchestrator interventions (alias: orch-intervention)
# Actions: pause_strategy, resume_strategy, emergency_stop, force_rebalance, adjust_allocation

# API server
genebot orchestrator-api <action>  # Manage orchestrator API server (alias: orch-api)
# Actions: start, stop

# Migration
genebot orchestrator-migrate <action>  # Migrate to orchestrator (alias: orch-migrate)
# Actions: analyze, backup, generate, migrate, validate, guide
```

### Monitoring & Analytics
```bash
# Real-time monitoring
genebot monitor                 # Real-time trading monitor
genebot trades                  # Show recent trades and P&L

# Reporting
genebot report                  # Generate comprehensive trading report
genebot analytics <type>        # Advanced analytics
# Types: performance, risk, correlation, attribution, optimization
```

### Security & Error Handling
```bash
# Security commands
genebot security <action>       # Security management
# Actions: validate-credentials, audit, scan-config, check-permissions

# Error handling
genebot error-report            # Generate error report
genebot health-check            # Comprehensive system health check
```

### Utilities & Maintenance
```bash
# System utilities
genebot completion              # Manage shell completion
genebot reset                   # Clean up all data and reset system
genebot --version              # Show version information
genebot --help                 # Show help and available commands

# File management
genebot data-export             # Export trading data
genebot data-import             # Import trading data
genebot cleanup                 # Clean up temporary files and logs
```

### Global Options
All commands support these global options:
```bash
--config-path <path>           # Path to configuration directory
--log-level <level>            # Set logging level (DEBUG, INFO, WARNING, ERROR)
--verbose, -v                  # Enable verbose output
--quiet, -q                    # Suppress all output except errors
--no-color                     # Disable colored output
--output-file <file>           # Write output to file
--dry-run                      # Show what would be done without making changes
--force                        # Force operation without confirmation
--auto-recover                 # Attempt automatic error recovery
```

## 🔧 Configuration

### Environment Configuration (.env)

The `.env` file controls GeneBot's runtime behavior and security settings:

#### Environment Modes
```bash
# ENVIRONMENT controls the trading mode
ENVIRONMENT=development    # Options: development, staging, production

# Development Mode:
# - Enhanced logging and debugging
# - Additional safety checks
# - Recommended for testing and learning

# Staging Mode:
# - Production-like environment
# - Used for final testing before live trading

# Production Mode:
# - Optimized for live trading
# - Minimal logging overhead
# - Maximum performance
```

#### Paper Trading vs Live Trading
```bash
# PAPER_TRADING controls whether to use real money
PAPER_TRADING=true        # true = demo/sandbox, false = live trading

# Always start with PAPER_TRADING=true for safety!
# Only set to false when you're confident in your setup
```

#### Risk Management Settings
```bash
# Global risk limits (applied across all accounts)
MAX_DAILY_LOSS=1000           # Stop trading if daily loss exceeds this
MAX_PORTFOLIO_RISK=0.02       # Maximum risk per trade (2% of portfolio)
PORTFOLIO_VALUE=100000        # Total portfolio value for risk calculations

# Position sizing
MAX_POSITION_SIZE=0.1         # Maximum position size (10% of portfolio)
MAX_OPEN_POSITIONS=5          # Maximum number of concurrent positions
```

#### API Credentials
```bash
# Crypto Exchange APIs
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_secret
BINANCE_SANDBOX=true          # Use testnet for safety

COINBASE_API_KEY=your_coinbase_key
COINBASE_API_SECRET=your_coinbase_secret
COINBASE_SANDBOX=true

# Forex Broker APIs
OANDA_API_KEY=your_oanda_key
OANDA_ACCOUNT_ID=your_account_id
OANDA_SANDBOX=true            # Use demo environment

# Interactive Brokers
IB_HOST=127.0.0.1
IB_PORT=7497                  # 7497 for paper trading, 7496 for live
IB_CLIENT_ID=1
```

### Account Configuration (config/accounts.yaml)

Define your trading accounts with specific settings:

```yaml
crypto_exchanges:
  binance-main:
    name: 'Binance Main Account'
    exchange_type: 'binance'
    api_key: '${BINANCE_API_KEY}'
    api_secret: '${BINANCE_API_SECRET}'
    sandbox: true                    # Use sandbox/testnet
    enabled: true                    # Enable/disable this account
    max_position_size: 1000          # Max position size in USD
    risk_limit: 0.02                 # Risk per trade (2%)
    trading_pairs: ['BTC/USDT', 'ETH/USDT', 'ADA/USDT']
    
  coinbase-demo:
    name: 'Coinbase Demo'
    exchange_type: 'coinbase'
    api_key: '${COINBASE_API_KEY}'
    api_secret: '${COINBASE_API_SECRET}'
    sandbox: true
    enabled: false                   # Disabled for now
    max_position_size: 500
    risk_limit: 0.01

forex_brokers:
  oanda-demo:
    name: 'OANDA Demo Account'
    broker_type: 'oanda'
    api_key: '${OANDA_API_KEY}'
    account_id: '${OANDA_ACCOUNT_ID}'
    sandbox: true
    enabled: true
    max_position_size: 10000         # Max position size in account currency
    leverage: 50                     # Maximum leverage
    currency_pairs: ['EUR/USD', 'GBP/USD', 'USD/JPY']
    
  ib-paper:
    name: 'Interactive Brokers Paper'
    broker_type: 'ib'
    host: '${IB_HOST}'
    port: 7497                       # Paper trading port
    client_id: 1
    enabled: true
    max_position_size: 5000
    leverage: 30
```

### Trading Strategy Configuration (config/trading_bot_config.yaml)

Configure your trading strategies and global settings. Multiple templates are available:

#### Available Configuration Templates
- **Development Template**: Safe defaults for testing and development
- **Production Template**: Optimized settings for live trading
- **Multi-Market Template**: Full multi-market configuration with arbitrage
- **Orchestrator Templates**: Various orchestrator configurations

#### Basic Configuration Example
```yaml
# Global Trading Settings
trading:
  max_position_size: 0.1             # 10% of portfolio per position
  risk_per_trade: 0.02               # 2% risk per trade
  max_drawdown: 0.15                 # Stop if drawdown exceeds 15%
  max_daily_trades: 10               # Limit daily trades
  trading_hours:
    start: "09:00"                   # Start trading time (UTC)
    end: "17:00"                     # End trading time (UTC)
    timezone: "UTC"

# Risk Management
risk_management:
  stop_loss_percentage: 0.02         # 2% stop loss
  take_profit_percentage: 0.04       # 4% take profit
  trailing_stop: true                # Enable trailing stops
  max_correlation: 0.7               # Max correlation between positions
  position_sizing_method: "fixed"    # fixed, percentage, volatility_adjusted

# Strategy Configuration
strategies:
  # Technical Analysis Strategies
  - name: "RSI_Mean_Reversion"
    type: "RSIStrategy"
    enabled: true
    markets: ["crypto", "forex"]     # Apply to both markets
    parameters:
      rsi_period: 14
      oversold_threshold: 30
      overbought_threshold: 70
      position_size: 0.05            # 5% of portfolio
      
  - name: "Moving_Average_Crossover"
    type: "MovingAverageStrategy"
    enabled: true
    markets: ["crypto"]              # Crypto only
    parameters:
      fast_ma: 10
      slow_ma: 20
      position_size: 0.03
      
  - name: "Multi_Indicator_Strategy"
    type: "MultiIndicatorStrategy"
    enabled: true
    markets: ["crypto", "forex"]
    parameters:
      rsi_period: 14
      macd_fast: 12
      macd_slow: 26
      bb_period: 20
      position_size: 0.04
      
  # Machine Learning Strategies
  - name: "ML_Pattern_Recognition"
    type: "MLPatternStrategy"
    enabled: false                   # Disabled by default
    markets: ["crypto"]
    parameters:
      lookback_period: 50
      prediction_horizon: 5
      confidence_threshold: 0.7
      position_size: 0.03
      
  # Arbitrage Strategies
  - name: "Cross_Market_Arbitrage"
    type: "CrossMarketArbitrageStrategy"
    enabled: true
    markets: ["crypto", "forex"]
    parameters:
      min_spread: 0.005              # Minimum 0.5% spread
      max_position_size: 0.1
      execution_timeout: 30
      
  - name: "Triangular_Arbitrage"
    type: "TriangularArbitrageStrategy"
    enabled: false
    markets: ["crypto"]
    parameters:
      min_profit: 0.003              # Minimum 0.3% profit
      max_slippage: 0.001
      
  # Forex-Specific Strategies
  - name: "Forex_Session_Strategy"
    type: "ForexSessionStrategy"
    enabled: false                   # Disabled
    markets: ["forex"]
    parameters:
      session: "london"              # london, new_york, tokyo, sydney
      volatility_threshold: 0.5
      position_size: 0.05
      
  - name: "Forex_Carry_Trade"
    type: "ForexCarryTradeStrategy"
    enabled: false
    markets: ["forex"]
    parameters:
      min_interest_diff: 0.02        # Minimum 2% interest rate difference
      position_size: 0.08

# Multi-Market Settings
multi_market:
  enabled: true
  cross_market_arbitrage: true       # Enable arbitrage opportunities
  correlation_threshold: 0.8         # Correlation limit for risk management
  max_exposure_per_market: 0.6       # Max 60% exposure per market type
  rebalancing_frequency: "daily"     # daily, weekly, monthly
  
  # Cross-market risk management
  risk_limits:
    max_total_exposure: 0.8          # Maximum total market exposure
    max_correlated_positions: 3      # Maximum correlated positions
    correlation_lookback: 30         # Days for correlation calculation

# Orchestrator Configuration (Optional)
orchestrator:
  enabled: false                     # Enable strategy orchestration
  allocation_method: "performance_based"  # equal_weight, performance_based, risk_parity
  rebalance_frequency: "daily"
  max_strategies: 5
  min_strategy_allocation: 0.1       # Minimum 10% allocation per strategy
  performance_lookback: 30           # Days for performance calculation
```

#### Orchestrator Configuration Example
```yaml
# Orchestrator-specific configuration
orchestrator:
  enabled: true
  allocation_method: "performance_based"
  rebalance_frequency: "daily"
  max_drawdown: 0.10
  
  # Strategy allocation settings
  allocation:
    min_allocation: 0.05             # Minimum 5% per strategy
    max_allocation: 0.40             # Maximum 40% per strategy
    rebalance_threshold: 0.05        # Rebalance if allocation drifts 5%
    
  # Performance monitoring
  performance:
    lookback_period: 30              # Days for performance calculation
    benchmark: "SPY"                 # Benchmark for comparison
    risk_free_rate: 0.02             # Risk-free rate for Sharpe calculation
    
  # Risk management
  risk:
    max_portfolio_var: 0.02          # Maximum portfolio VaR
    correlation_threshold: 0.7       # Maximum strategy correlation
    stress_test_scenarios: ["market_crash", "high_volatility"]
```

## 📚 Step-by-Step Tutorials

### Tutorial 1: Complete Setup from Scratch

#### Step 1: Install and Initialize
```bash
# Install GeneBot
pip install genebot

# Initialize workspace
genebot init-config

# Check what was created
ls -la
```

#### Step 2: Configure Environment
```bash
# Edit the .env file
nano .env

# Set basic configuration:
ENVIRONMENT=development
PAPER_TRADING=true
MAX_DAILY_LOSS=500
PORTFOLIO_VALUE=10000
```

#### Step 3: Set Up Demo Accounts
```bash
# Set up demo accounts automatically
genebot setup-demo

# Verify accounts were created
genebot list

# Validate configuration
genebot validate
```

#### Step 4: Start Trading
```bash
# Start the bot
genebot start

# Check status in another terminal
genebot status

# View logs
tail -f logs/trading_bot.log
```

### Tutorial 2: Adding Real Exchange Accounts

#### Step 1: Get API Credentials
1. **Binance**: Go to Binance.com → Account → API Management
2. **OANDA**: Go to OANDA → My Account → Manage API Access
3. **Create API keys with appropriate permissions**

#### Step 2: Add Credentials to Environment
```bash
# Edit .env file
nano .env

# Add your real API credentials
BINANCE_API_KEY=your_real_binance_key
BINANCE_API_SECRET=your_real_binance_secret
BINANCE_SANDBOX=true  # Keep as true for testing

OANDA_API_KEY=your_real_oanda_key
OANDA_ACCOUNT_ID=your_real_account_id
OANDA_SANDBOX=true    # Keep as true for testing
```

#### Step 3: Add Accounts Using CLI
```bash
# Add Binance account (interactive)
genebot add-crypto binance --mode demo

# Follow the prompts:
# - Account name: binance-main
# - Enable account: yes
# - Max position size: 1000
# - Risk limit: 0.02

# Add OANDA account (interactive)
genebot add-forex oanda --mode demo

# Follow the prompts:
# - Account name: oanda-main
# - Enable account: yes
# - Max position size: 5000
# - Leverage: 30
```

#### Step 4: Validate and Test
```bash
# Validate all accounts
genebot validate-accounts

# List configured accounts
genebot list

# Test with paper trading first
genebot start
```

### Tutorial 3: Custom Strategy Configuration

#### Step 1: Edit Strategy Configuration
```bash
# Edit the trading configuration
nano config/trading_bot_config.yaml
```

#### Step 2: Add Custom Strategy
```yaml
strategies:
  - name: "My_Custom_RSI"
    enabled: true
    markets: ["crypto"]
    parameters:
      rsi_period: 21          # Custom RSI period
      oversold_threshold: 25  # More aggressive oversold
      overbought_threshold: 75 # More aggressive overbought
      position_size: 0.03     # 3% position size
      stop_loss: 0.02         # 2% stop loss
      take_profit: 0.06       # 6% take profit
```

#### Step 3: Test Strategy
```bash
# Validate configuration
genebot validate

# Start with paper trading
PAPER_TRADING=true genebot start

# Monitor performance
genebot status
genebot report
```

### Tutorial 4: Multi-Market Arbitrage Setup

#### Step 1: Enable Multi-Market Features
```bash
# Edit trading configuration
nano config/trading_bot_config.yaml
```

#### Step 2: Configure Arbitrage Settings
```yaml
multi_market:
  cross_market_arbitrage: true
  correlation_threshold: 0.8
  max_exposure_per_market: 0.5
  arbitrage_min_profit: 0.005    # Minimum 0.5% profit
  
strategies:
  - name: "Cross_Market_Arbitrage"
    enabled: true
    markets: ["crypto", "forex"]
    parameters:
      min_spread: 0.005
      max_position_size: 0.1
      execution_timeout: 30
```

#### Step 3: Add Multiple Exchange Accounts
```bash
# Add multiple crypto exchanges
genebot add-crypto binance --mode demo
genebot add-crypto coinbase --mode demo

# Add forex brokers
genebot add-forex oanda --mode demo
genebot add-forex ib --mode demo

# Validate all accounts
genebot validate
```

### Tutorial 5: Production Deployment

#### Step 1: Switch to Production Mode
```bash
# Edit environment for production
nano .env

# Update settings:
ENVIRONMENT=production
PAPER_TRADING=false        # CAREFUL: This uses real money!
MAX_DAILY_LOSS=2000       # Increase limits for production
PORTFOLIO_VALUE=50000
```

#### Step 2: Enable Real Trading Accounts
```bash
# Edit account configuration
nano config/accounts.yaml

# Change sandbox settings:
crypto_exchanges:
  binance-main:
    sandbox: false          # Use real trading
    enabled: true
```

#### Step 3: Final Validation and Deployment
```bash
# Comprehensive validation
genebot validate
genebot health-check

# Backup configuration
genebot backup-config

# Start production trading
genebot start

# Monitor closely
watch -n 5 'genebot status'
```

### Advanced Configuration Tips

#### 1. Environment-Specific Settings
```bash
# Use different settings for different environments
# Development
ENVIRONMENT=development
PAPER_TRADING=true
MAX_DAILY_LOSS=100

# Production
ENVIRONMENT=production
PAPER_TRADING=false
MAX_DAILY_LOSS=5000
```

#### 2. Security Best Practices
```bash
# Never commit real API keys to version control
# Use environment variables for sensitive data
# Enable IP whitelisting on exchanges
# Use read-only API keys when possible
# Regularly rotate API keys
```

#### 3. Testing Configuration
```bash
# Always test with demo accounts first
genebot setup-demo
genebot validate
genebot start

# Monitor logs for any issues
tail -f logs/trading_bot.log
```

#### 4. Monitoring and Maintenance
```bash
# Regular health checks
genebot health-check

# Generate reports
genebot report

# Backup configurations
genebot backup-config

# Update strategies based on performance
nano config/trading_bot_config.yaml
```

## 📊 Supported Markets & Exchanges

### Cryptocurrency Exchanges
| Exchange | Spot Trading | Futures | Sandbox | Status |
|----------|-------------|---------|---------|--------|
| Binance | ✅ | ✅ | ✅ | Active |
| Coinbase | ✅ | ❌ | ✅ | Active |
| Kraken | ✅ | ✅ | ✅ | Active |
| KuCoin | ✅ | ✅ | ✅ | Active |
| Bybit | ✅ | ✅ | ✅ | Active |

### Forex Brokers
| Broker | Spot Forex | CFDs | Demo | Status |
|--------|------------|------|------|--------|
| OANDA | ✅ | ✅ | ✅ | Active |
| MetaTrader 5 | ✅ | ✅ | ✅ | Active |
| Interactive Brokers | ✅ | ✅ | ✅ | Active |

## 🧪 Testing & Development

### Run Tests
```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_strategies.py
pytest tests/test_risk_management.py
pytest tests/test_multi_market.py

# Run with coverage
pytest --cov=genebot
```

### Development Setup
```bash
# Install development dependencies
pip install -e ".[dev]"

# Run code formatting
black genebot/
flake8 genebot/

# Type checking
mypy genebot/
```

## 📈 Performance & Monitoring

### Grafana Dashboards
- **Trading Overview**: Real-time P&L, positions, and performance
- **Risk Monitoring**: Drawdown, exposure, and risk metrics
- **Multi-Market Analysis**: Cross-market correlations and arbitrage
- **System Health**: Bot status, API health, and system metrics

### Prometheus Metrics
- Trading performance metrics
- Risk management indicators
- System health and uptime
- API response times and errors

## 🔒 Security & Compliance

### Security Features
- **Encrypted Credential Storage**: API keys stored securely
- **Live API Validation**: Real-time credential verification
- **Audit Trails**: Complete trading history logging
- **Access Controls**: Role-based permission system

### Compliance Support
- **Regulatory Reporting**: Automated compliance reports
- **Trade Surveillance**: Real-time monitoring for suspicious activity
- **Risk Limits**: Configurable risk and exposure limits
- **Documentation**: Comprehensive audit documentation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "No accounts configured yet"
```bash
# Solution: Initialize and set up accounts
genebot init-config
genebot list-accounts
# If no accounts exist:
genebot add-crypto binance --mode demo
genebot add-forex oanda --mode demo
```

#### Issue: "API credentials invalid" or "Authentication failed"
```bash
# Solution: Check your .env file and API keys
nano .env
genebot validate-accounts
genebot security validate-credentials

# Common causes:
# - Incorrect API keys or secrets
# - API keys don't have required permissions
# - IP address not whitelisted on exchange
# - Using production keys with sandbox=true (or vice versa)
```

#### Issue: "Strategy not found" or "Strategy failed to load"
```bash
# Solution: Check strategy configuration and availability
genebot list-strategies
genebot validate-config

# Check strategy name in config/trading_bot_config.yaml
# Ensure strategy type matches available strategies
```

#### Issue: "Orchestrator failed to start"
```bash
# Solution: Check orchestrator configuration
genebot orchestrator-config validate
genebot system-validate

# Common causes:
# - Invalid orchestrator configuration
# - Conflicting strategy allocations
# - Missing required strategies
```

#### Issue: "Permission denied" or "Access denied" errors
```bash
# Solution: Check file permissions and API key permissions
ls -la config/
chmod 600 .env  # Secure environment file
genebot security check-permissions

# For API keys:
# - Ensure keys have trading permissions enabled
# - Verify IP whitelisting settings on exchange
# - Check if API key is expired or suspended
```

#### Issue: Bot won't start or crashes immediately
```bash
# Solution: Comprehensive diagnostics
genebot validate-config
genebot system-validate
genebot health-check

# Check logs for specific errors
genebot instance-logs main
tail -f logs/genebot.log

# Common causes:
# - Invalid configuration files
# - Missing dependencies
# - Port conflicts
# - Insufficient system resources
```

#### Issue: "Module not found" or import errors
```bash
# Solution: Reinstall GeneBot and dependencies
pip uninstall genebot
pip install --upgrade genebot
genebot --version

# For development installations:
pip install -e ".[all]"
```

#### Issue: Strategies not executing trades
```bash
# Solution: Check strategy status and market conditions
genebot status --detailed
genebot monitor
genebot list-strategies

# Common causes:
# - Strategies disabled in configuration
# - Insufficient account balance
# - Market conditions don't meet strategy criteria
# - Risk limits preventing trades
```

#### Issue: High memory usage or performance issues
```bash
# Solution: Check system resources and optimize
genebot instance-metrics main
genebot analytics performance

# Optimization steps:
# - Reduce number of active strategies
# - Increase monitoring intervals
# - Clean up old log files
# - Restart bot instances periodically
```

#### Issue: Cross-market arbitrage not working
```bash
# Solution: Check multi-market configuration
genebot validate-config
# Verify in config/trading_bot_config.yaml:
# multi_market.enabled: true
# multi_market.cross_market_arbitrage: true

# Check account connectivity for both markets
genebot validate-accounts
```

#### Issue: Orchestrator allocation issues
```bash
# Solution: Check orchestrator allocation settings
genebot orchestrator-config show
genebot orchestrator-status --verbose

# Common causes:
# - Allocation percentages don't sum to 1.0
# - Strategy performance data insufficient
# - Risk limits preventing allocation changes
```

### Advanced Troubleshooting

#### Enable Debug Logging
```bash
# Temporary debug mode
genebot start --log-level DEBUG

# Or edit config/logging_config.yaml:
# level: DEBUG
```

#### Generate Comprehensive Error Report
```bash
# Generate detailed error report
genebot error-report

# Security audit
genebot security audit

# System validation report
genebot system-validate --verbose
```

#### Check System Dependencies
```bash
# Verify Python version and dependencies
python --version
pip list | grep -E "(ccxt|pandas|numpy|ta-lib)"

# Check system resources
df -h  # Disk space
free -h  # Memory usage
```

### Getting Help

#### Configuration Assistance
```bash
# Get comprehensive configuration help
genebot config-help

# Validate all components
genebot system-validate --verbose
genebot health-check
```

#### Log Analysis
```bash
# View real-time logs
tail -f logs/genebot.log

# View error logs
tail -f logs/errors.log

# View specific instance logs
genebot instance-logs <instance_name>

# View all available logs
ls -la logs/
```

#### Performance Monitoring
```bash
# Monitor system performance
genebot monitor --refresh 10
genebot instance-metrics main
genebot analytics performance
```

#### Complete System Reset
```bash
# If all else fails, reset everything (CAUTION: This removes all data)
genebot config-backup  # Backup first!
genebot reset
genebot init-config --template development
genebot add-crypto binance --mode demo
genebot add-forex oanda --mode demo
genebot validate
```

### Emergency Procedures

#### Emergency Stop All Trading
```bash
# Stop all trading immediately
genebot stop --force
genebot orchestrator-intervention emergency_stop --reason "Emergency stop"

# Close all open positions (if needed)
# Note: This command should be used with extreme caution
# genebot close-all-orders --confirm
```

#### Recovery from System Failure
```bash
# 1. Stop all processes
genebot stop --force
genebot stop-monitoring

# 2. Check system integrity
genebot system-validate
genebot health-check

# 3. Restore from backup if needed
genebot config-restore

# 4. Restart with validation
genebot validate-config
genebot start
```

## 🆘 Support

### Documentation
- [User Guide](docs/USER_GUIDE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Strategy Development Guide](docs/STRATEGY_DEVELOPMENT_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md)

### Community
- **GitHub Issues**: [Report bugs and request features](https://github.com/genebot/genebot/issues)
- **Discussions**: [Community discussions and Q&A](https://github.com/genebot/genebot/discussions)
- **Discord**: [Join our Discord server](https://discord.gg/genebot)

### Professional Support
- **Email**: support@genebot.ai
- **Enterprise Support**: enterprise@genebot.ai

## ⚠️ Disclaimer

**IMPORTANT**: Trading involves substantial risk of loss and is not suitable for all investors. Past performance is not indicative of future results. GeneBot is provided for educational and research purposes. Always test strategies thoroughly in demo environments before live trading.

**USE AT YOUR OWN RISK**: The developers of GeneBot are not responsible for any financial losses incurred through the use of this software.

## 🎯 Roadmap

### Version 1.1.28 (Q2 2024)
- [ ] Advanced ML strategies
- [ ] Social trading features
- [ ] Mobile app companion
- [ ] Enhanced backtesting

### Version 1.1.28 (Q3 2024)
- [ ] Options trading support
- [ ] Advanced portfolio optimization
- [ ] Institutional features
- [ ] API marketplace

---

**Made with ❤️ by the GeneBot Team**

*Empowering traders with advanced automation and intelligence.*