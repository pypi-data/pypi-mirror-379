# SQLite MCP Server

*Last Updated: September 22, 2025 - v2.6.0 JSON Helper Tools Release*

[![Docker Pulls](https://img.shields.io/docker/pulls/writenotenow/sqlite-mcp-server)](https://hub.docker.com/r/writenotenow/sqlite-mcp-server)
![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-2.6.0-green)
[![GitHub Stars](https://img.shields.io/github/stars/neverinfamous/sqlite-mcp-server?style=social)](https://github.com/neverinfamous/sqlite-mcp-server)

---

## 📋 Table of Contents

### Quick Start
- [🚀 Quick Try](#-quick-try)
- [✅ Quick Test - Verify Everything Works](#-quick-test---verify-everything-works)
- [📦 Getting Started](#-getting-started)

### Core Information
- [🔍 Overview](#-overview)
- [⭐ Key Features](#-key-features)

### Installation & Configuration
- [📋 Installation Requirements](#-installation-requirements)
- [🐍 Quick Start (Python)](#-quick-start-python)
- [⚙️ MCP Client Configuration](#-mcp-client-configuration)
- [🐳 Docker Hub Deployment](#-docker-hub-deployment)
- [🗄️ Database Configuration](#-database-configuration)

### Core Features & Tools
- [🛡️ Security & Data Integrity](#️-security--data-integrity)
  - [Parameter Binding Security](#parameter-binding-security-v260)
  - [💾 JSONB Binary Storage](#jsonb-binary-storage)
  - [🔒 Transaction Safety](#transaction-safety)
  - [🔗 Foreign Key Enforcement](#foreign-key-enforcement)
- [🎯 JSON Helper Tools](#-json-helper-tools) - NEW in v2.6.0

### Advanced Features
- [📝 Advanced Text Processing](#-advanced-text-processing)
- [📈 Statistical Analysis Library](#-statistical-analysis-library)
- [🔍 Full-Text Search (FTS5)](#-full-text-search-fts5)
- [💾 Backup & Restore Operations](#-backup--restore-operations)
- [⚙️ Advanced PRAGMA Operations](#-advanced-pragma-operations)
- [📊 Virtual Table Management](#-virtual-table-management)
- [🧠 Semantic/Vector Search](#-semanticvector-search)
- [🌍 SpatiaLite Geospatial Analytics](#-spatialite-geospatial-analytics)
- [📋 Enhanced Virtual Tables](#-enhanced-virtual-tables)
- [⚡ Vector Index Optimization](#-vector-index-optimization)
- [🤖 Intelligent MCP Resources & Prompts](#-intelligent-mcp-resources--prompts)

### Usage & Best Practices
- [✅ Best Practices for Using SQLite MCP](#-best-practices-for-using-sqlite-mcp)
- [🔧 Troubleshooting](#-troubleshooting)

### Project Information
- [🤝 Contributing](#-contributing)
- [🔒 Security](#-security)
- [🔗 Additional Resources](#-additional-resources)
- [💬 Support](#-support)
- [📄 License](#-license)
- [🏷️ Attribution](#-attribution)

---

## 🚀 Quick Try

Run instantly with Docker (creates a project-local database):

```bash
docker run -i --rm \
  -v $(pwd):/workspace \
  writenotenow/sqlite-mcp-server:latest \
  --db-path /workspace/sqlite_mcp.db
```

---

## 🔍 Overview

The SQLite MCP Server transforms SQLite into a powerful, AI-ready database engine. It combines standard relational operations with advanced analytics, text and vector search, geospatial capabilities, and intelligent workflow automation. By layering business intelligence tools, semantic resources, and guided prompts on top of SQLite, it enables both developers and AI assistants to interact with data more naturally and effectively.

This makes it not just a database interface, but a **workflow-aware assistant** for developers and AI systems.

---

## ⭐ Key Features

* **JSON Helper Tools (6 tools) - NEW v2.6.0**: Parameter serialization, auto-normalization, JSONB binary storage, enhanced error diagnostics
* **Advanced Text Processing (8 tools)**: Regex, fuzzy match, phonetic, similarity, normalization, validation
* **Statistical Analysis (8 tools)**: Descriptive stats, percentiles, time series analysis
* **Advanced SQL Support**: Complex queries including window functions, subqueries, and advanced filtering
* **Business Intelligence**: Integrated memo resource for capturing business insights during analysis
* **Enhanced Error Handling**: Detailed diagnostics with specific fix suggestions
* **Multi-Level Caching**: Hierarchical caching for optimal performance
* **Pattern Recognition**: Automatic optimization of frequent queries
* **JSON Validation**: Prevents invalid JSON from being stored in the database
* **WAL Mode Compatible**: Works alongside the existing Write-Ahead Logging (WAL) journal mode
* **Comprehensive Schema Tools**: Enhanced tools for exploring and documenting database structure
* **Core Database (15 tools)**: Essential CRUD operations, schema management, and database administration
* **Full-Text Search (3 tools)**: FTS5 implementation with BM25 ranking and snippets
* **Backup/Restore (5 tools)**: Enterprise-grade backup with integrity verification and safety confirmations
* **PRAGMA Operations (5 tools)**: SQLite configuration, optimization, and introspection tools
* **Virtual Tables (6 tools)**: R-Tree spatial indexing, CSV import/export, and virtual table management
* **Enhanced Virtual Tables (4 tools)**: Smart CSV/JSON import with automatic schema inference
* **SpatiaLite Geospatial (7 tools)**: Enterprise GIS with spatial indexing, geometric operations, and Windows compatibility
* **Semantic/Vector Search (6 tools)**: AI-native semantic search with embedding storage and hybrid ranking
* **Vector Index Optimization (4 tools)**: ANN search with k-means clustering for sub-linear O(log n) performance
* **MCP Resources (7)**: Dynamic database meta-awareness with real-time schema and performance insights
* **MCP Prompts (7)**: Intelligent workflow automation with semantic query translation and optimization

## 📊 Tool Categories at a Glance

**73 Total Tools Across 14 Categories** (enterprise-scale but modular - users can disable extras):

- **🎯 JSON Helper Tools (6)** - NEW v2.6.0: Complete JSON manipulation suite
- **📊 Core Database (15)** - Essential CRUD operations and schema management  
- **📝 Advanced Text Processing (8)** - Regex, fuzzy matching, similarity analysis
- **📈 Statistical Analysis (8)** - Descriptive stats, percentiles, time series
- **🔍 Full-Text Search (3)** - FTS5 search, indexing, and content management
- **💾 Backup & Restore (5)** - Database backup, restore, and migration tools
- **⚙️ PRAGMA Operations (5)** - Database configuration and optimization
- **📋 Virtual Tables (6)** - CSV import/export and virtual table management
- **📊 Enhanced Virtual Tables (4)** - Smart CSV/JSON import with automatic schema inference
- **🧠 Semantic/Vector Search (6)** - Embeddings and similarity search
- **🌍 Geospatial (SpatiaLite) (7)** - Spatial data analysis and operations
- **⚡ Performance Optimization (4)** - Vector indexing and ANN search optimization
- **🤖 MCP Resources (7)** - Dynamic database meta-awareness resources
- **🔒 Security & Validation (5)** - SQL injection protection and JSON validation

**⚠️ Tool Count Consideration**
The server exposes **73 tools** by default. MCP clients (e.g., Cursor) may warn around 80 tools and can become unstable past \~100–120. You can disable unneeded tools in client settings to slim down usage for your workflow.

**📝 Note**: MCP Resources (7) and Prompts (7) are separate from the tool count - they provide metadata and workflow guidance but don't count toward the 73-tool limit.

### 🔧 Available Tools, Resources & Prompts

#### **Core Database Tools** (15 tools)
| Tool | Description |
|------|-------------|
| `read_query` | Execute SELECT queries on the SQLite database |
| `write_query` | Execute INSERT, UPDATE, or DELETE queries |
| `create_table` | Create new tables in the database |
| `list_tables` | List all tables in the database |
| `describe_table` | Get schema information for a specific table |
| `append_insight` | Add business insights to the memo |
| `vacuum_database` | Optimize database by reclaiming unused space |
| `analyze_database` | Update database statistics for query optimization |
| `integrity_check` | Check database integrity and report corruption |
| `database_stats` | Get database performance and usage statistics |
| `index_usage_stats` | Get index usage statistics for optimization |
| `backup_database` | Create database backups to files |
| `restore_database` | Restore database from backup files |
| `verify_backup` | Verify integrity of backup files |
| `pragma_settings` | Get/set SQLite PRAGMA configuration settings |

#### **JSON Helper Tools** (6 tools) - NEW in v2.6.0

These tools provide complete JSON manipulation capabilities with automatic parameter serialization, intelligent auto-normalization, and enhanced error diagnostics for seamless database operations.

| Tool | Description |
|------|-------------|
| `json_insert` | Insert JSON data with automatic serialization and validation |
| `json_update` | Update JSON fields by path with precision targeting |
| `json_select` | Extract JSON data with flexible output formats |
| `json_query_complex` | Advanced JSON filtering and querying operations |
| `json_merge` | Intelligent JSON object merging with conflict resolution |
| `json_validate_security` | Security-focused JSON validation with threat detection |

#### **Advanced PRAGMA Operations** (5 tools)
| Tool | Description |
|------|-------------|
| `pragma_optimize` | Run PRAGMA optimize for performance improvements |
| `pragma_table_info` | Get detailed table schema using PRAGMA table_info |
| `pragma_database_list` | List all attached databases with file paths |
| `pragma_compile_options` | Show SQLite compile-time options and capabilities |

#### **Full-Text Search (FTS5)** (3 tools)
| Tool | Description |
|------|-------------|
| `create_fts_table` | Create FTS5 virtual tables for full-text search |
| `rebuild_fts_index` | Rebuild FTS5 indexes for optimal performance |
| `fts_search` | Perform enhanced full-text search with ranking and snippets |

#### **Virtual Table Management** (6 tools)
| Tool | Description |
|------|-------------|
| `create_rtree_table` | Create R-Tree virtual tables for spatial indexing |
| `create_csv_table` | Create virtual tables to access CSV files |
| `create_series_table` | Create generate_series virtual tables for sequences |
| `list_virtual_tables` | List all virtual tables in the database |
| `drop_virtual_table` | Drop virtual tables with confirmation |
| `virtual_table_info` | Get detailed information about virtual tables |

#### **Enhanced Virtual Tables** (4 tools)
| Tool | Description |
|------|-------------|
| `create_enhanced_csv_table` | Create CSV tables with automatic data type inference |
| `create_json_collection_table` | Create virtual tables for JSON file collections (JSONL, arrays) |
| `analyze_csv_schema` | Analyze CSV files and infer data types without creating tables |
| `analyze_json_schema` | Analyze JSON file collections and infer schema |

#### **Geospatial (SpatiaLite)** (7 tools)
| Tool | Description |
|------|-------------|
| `load_spatialite` | Load SpatiaLite extension for geospatial capabilities |
| `create_spatial_table` | Create spatial tables with geometry columns |
| `spatial_index` | Create or drop spatial indexes on geometry columns |
| `spatial_query` | Execute spatial queries with geometric operations |
| `geometry_operations` | Common geometry operations (buffer, intersection, union, etc.) |
| `import_shapefile` | Import Shapefile data into spatial tables |
| `spatial_analysis` | Perform spatial analysis (nearest neighbor, spatial join, etc.) |

#### **Semantic Search & Embeddings** (6 tools)
| Tool | Description |
|------|-------------|
| `create_embeddings_table` | Create tables optimized for storing embeddings with metadata |
| `store_embedding` | Store embedding vectors with associated metadata |
| `semantic_search` | Perform semantic similarity search using cosine similarity |
| `hybrid_search` | Combine FTS5 keyword search with semantic similarity |
| `calculate_similarity` | Calculate cosine similarity between embedding vectors |
| `batch_similarity_search` | Perform similarity search with multiple query vectors |
#### **Vector Index Optimization** (4 tools)
| Tool | Description |
|------|-------------|
| `create_vector_index` | Create optimized indexes for vector similarity search |
| `optimize_vector_search` | Perform optimized vector similarity search using indexes |
| `analyze_vector_index` | Analyze vector index performance and statistics |
| `rebuild_vector_index` | Rebuild vector indexes for optimal performance |

#### **Statistical Analysis** (8 tools)
| Tool | Description |
|------|-------------|
| `descriptive_statistics` | Calculate comprehensive descriptive statistics for numeric columns |
| `correlation_analysis` | Calculate correlation coefficients between numeric columns |
| `percentile_analysis` | Calculate percentiles and quartiles for numeric columns |
| `distribution_analysis` | Analyze distribution (skewness, kurtosis, normality) |
| `moving_averages` | Calculate moving averages and trend analysis for time series |
| `outlier_detection` | Detect outliers using IQR method and Z-score analysis |
| `regression_analysis` | Perform linear regression analysis between variables |
| `hypothesis_testing` | Perform statistical hypothesis tests (t-test, chi-square) |

#### **Text Processing & Advanced Search** (8 tools)
| Tool | Description |
|------|-------------|
| `regex_extract` | Extract text using PCRE-style regular expressions |
| `regex_replace` | Replace text using PCRE-style regular expressions |
| `fuzzy_match` | Find fuzzy matches using Levenshtein distance |
| `phonetic_match` | Find phonetic matches using Soundex and Metaphone |
| `text_similarity` | Calculate text similarity between columns or reference text |
| `text_normalize` | Normalize text with various transformations |
| `advanced_search` | Advanced search combining multiple text processing techniques |
| `text_validation` | Validate text against various patterns and rules |

---

#### **📊 MCP Resources** (7 resources)
| Resource | URI | Description |
|----------|-----|-------------|
| Database Schema | `database://schema` | Complete database schema with tables, columns, indexes, and relationships |
| Server Capabilities | `database://capabilities` | Comprehensive server capabilities matrix including all tools and features |
| Table Statistics | `database://statistics` | Real-time database statistics, table sizes, row counts, and optimization recommendations |
| Search Index Status | `database://search_indexes` | Status of FTS5 full-text search and semantic search indexes with performance metrics |
| Performance Insights | `database://performance` | Database performance analysis, optimization tips, and health recommendations |
| Business Insights Memo | `memo://insights` | A living document of discovered business insights |
| JSON Diagnostics | `diagnostics://json` | Diagnostic information about JSON handling capabilities |

---

#### **🎯 MCP Prompts** (7 prompts)
| Prompt | Description |
|--------|-------------|
| `semantic_query` | Guide for translating natural language queries into semantic search + SQL operations |
| `summarize_table` | Intelligent table analysis and summary generation with key statistics |
| `optimize_database` | Step-by-step database optimization workflow with performance analysis |
| `setup_semantic_search` | Complete guide for setting up semantic search with embeddings |
| `hybrid_search_workflow` | Step-by-step implementation of hybrid keyword + semantic search |
| `mcp-demo` | Seed database with initial data and demonstrate SQLite MCP Server capabilities |
| `json-diagnostic` | Check SQLite JSONB capabilities and run diagnostics |

---

## ✅ Quick Test - Verify Everything Works

**Test all 73 tools in 30 seconds:**

```bash
# Quick smoke test (includes JSON helper tools)
python test_runner.py --quick

# Test JSON helper tools specifically
python test_runner.py --quick --json

# Standard comprehensive test (recommended)
python test_runner.py --standard

# Full test suite with edge cases
python test_runner.py --full
```

**Expected output:**
```
🚀 SQLite MCP Server Comprehensive Test Suite v2.6.0
================================================================

🔍 Environment Detection:
  ✅ SQLite 3.50.4 (JSONB supported)
  ✅ Python 3.12.11  
  ✅ MCP 1.14.0

📊 Testing 73 Tools across 14 categories...

✅ Core Database Operations (15/15 passed)
✅ JSON Helper Tools (6/6 passed) - NEW in v2.6.0
✅ Legacy Raw JSON SQL Ops (6/6 passed)
✅ Text Processing (8/8 passed)
✅ Statistical Analysis (8/8 passed)
✅ Advanced PRAGMA Operations (5/5 passed)
🎉 SUCCESS: 73/73 tools tested successfully!

**📝 Note on Legacy JSON Operations:** Legacy JSON SQL operations remain available (e.g., `json_extract`, `json_set`, `json_array`) - these are standard SQLite functions, not separate MCP tools. New projects should prefer JSON Helper Tools for enhanced security, auto-normalization, and better error diagnostics.

🎯 JSON Tools Status: ACTIVE
✅ 6 JSON helper tools: OPERATIONAL
✅ Auto-normalization: ENABLED
✅ Parameter serialization: ACTIVE
```

### 🛡️ **Security Testing - SQL Injection Protection**

**TL;DR:** Critical injection vectors blocked, parameter binding validated — overall posture: **STRONG** 🛡️

**NEW: Comprehensive SQL injection vulnerability testing**

```bash
# Test SQL injection protection (from tests directory)
cd tests && python test_sql_injection.py

# Expected result: 🛡️ Overall security posture: STRONG
```

**What it tests:**
- **Protection against the SQL injection vulnerability** found in original Anthropic SQLite MCP server
- **11 different attack vectors** including multiple statements, UNION injection, blind injection
- **Parameter binding protection** with malicious payloads
- **Stacked queries and comment-based injection** attempts

**Attack Vectors Tested:**
1. **Multiple Statement Injection** - `SELECT 1; DROP TABLE users;` ✅ BLOCKED
2. **UNION-based Information Disclosure** - `SELECT username UNION SELECT password_hash` ⚠️ Executes (but safe, as these are legitimate SELECT queries, not injection)
3. **Boolean-based Blind Injection** - Conditional queries to extract data ⚠️ Executes (but safe, as these are legitimate SELECT queries, not injection)
4. **Time-based Blind Injection** - Queries that could cause delays ⚠️ Executes (but safe, as these are legitimate SELECT queries, not injection)
5. **Comment-based Injection** - Using `--`, `/* */`, and `#` comments ✅ MOSTLY BLOCKED
6. **Stacked Queries with Various Separators** - Different line endings ✅ BLOCKED
7. **Parameter Binding Protection** - 6 malicious payloads with safe binding ✅ ALL SAFE
8. **String Concatenation Demo** - Shows what would happen with unsafe code ⚠️ EDUCATIONAL

**Security Assessment:**
- ✅ **Critical attacks blocked**: Multiple statements, stacked queries
- ✅ **Parameter binding working**: All malicious payloads safely neutralized
- ⚠️ **Complex SELECT queries execute**: This is expected behavior for valid SQL
- 🛡️ **Overall security posture: STRONG**

**Note**: Error messages in the output are **expected** - they show the security protections working correctly by rejecting malicious queries.

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 📦 Getting Started

### 📋 Installation Requirements

* **Python 3.10+** – required runtime
* **SQLite 3.45.0+** – with JSONB support (current: 3.50.4)
* **MCP 1.14.0+** – Model Context Protocol library

**Optional (advanced users):**

* **Node.js 18+** – extra JSONB utilities (ESLint compliant)
* **Visual Studio C++ Build Tools** – only for Node.js + better-sqlite3
* ⚠️ Core server is Python-only and works without Node.js

### Known Minor Issues

* **JSON formatting**: Always use valid JSON with double quotes
* **Complex queries**: Use parameter binding for advanced queries

### 🐍 Quick Start (Python)

```bash
# Auto-detect project root (default)
python start_sqlite_mcp.py

# Create organized data directory
python start_sqlite_mcp.py --create-data-dir

# Use specific database
python start_sqlite_mcp.py --db-path /path/to/database.db

# In-memory (testing only)
python start_sqlite_mcp.py --db-path :memory:
```

### ⚙️ MCP Client Configuration

**Local Python:**

```json
{
  "mcpServers": {
    "sqlite-mcp-server": {
      "command": "python",
      "args": [
        "/path/to/sqlite-mcp-server/start_sqlite_mcp.py",
        "--db-path", "/path/to/database.db"
      ]
    }
  }
}
```

**Docker:**

```json
{
  "mcpServers": {
    "sqlite-mcp-server": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "/host/project:/workspace",
        "writenotenow/sqlite-mcp-server:latest",
        "--db-path", "/workspace/database.db"
      ]
    }
  }
}
```

### 🐳 Docker Hub Deployment

Available on Docker Hub at [`writenotenow/sqlite-mcp-server`](https://hub.docker.com/r/writenotenow/sqlite-mcp-server).

```bash
# Pull latest version
docker pull writenotenow/sqlite-mcp-server:latest

# Pull specific version
docker pull writenotenow/sqlite-mcp-server:v2.6.0
```

---

## 📝 Advanced Text Processing

The SQLite MCP Server v2.6.0 includes a comprehensive text processing toolkit with 8 specialized functions for advanced text analysis, pattern matching, and data cleaning. This brings the total server capabilities to **73 tools** for complete database and text processing operations.

**📚 See [Real-World Use Cases](https://gist.github.com/neverinfamous/7d36fb5676c5767e5c5aad4250244887) for complete text analysis workflows and advanced pattern matching use cases.**

### Available Text Processing Functions

**Pattern Extraction & Replacement:**
```javascript
// Extract email addresses using regex patterns
{
  "table_name": "users",
  "column_name": "contact_info", 
  "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
  "flags": "i"
}
```

**Fuzzy & Phonetic Matching:**
```javascript
// Find similar names using fuzzy matching
{
  "table_name": "customers",
  "column_name": "name",
  "search_term": "John Smith",
  "threshold": 0.8
}
```

**Text Similarity & Analysis:**
```javascript
// Calculate text similarity between columns
{
  "table_name": "products",
  "column_name": "description",
  "compare_column": "summary",
  "method": "cosine"
}
```

**Text Normalization & Validation:**
```javascript
// Normalize text with multiple operations
{
  "table_name": "reviews",
  "column_name": "comment",
  "operations": ["lowercase", "trim", "remove_extra_spaces"]
}
```

### Text Processing Tools

1. **`regex_extract`**: Extract text patterns using PCRE-style regular expressions with capture groups
2. **`regex_replace`**: Replace text patterns with support for backreferences and preview mode
3. **`fuzzy_match`**: Find similar text using Levenshtein distance and sequence matching
4. **`phonetic_match`**: Match text phonetically using Soundex and Metaphone algorithms
5. **`text_similarity`**: Calculate similarity between text columns using Cosine, Jaccard, or Levenshtein methods
6. **`text_normalize`**: Apply multiple text normalization operations (case, Unicode, whitespace, etc.)
7. **`advanced_search`**: Multi-method search combining exact, fuzzy, regex, word boundary, and phonetic matching
8. **`text_validation`**: Validate text against common patterns (email, phone, URL, credit card, etc.)

---

## 📈 Statistical Analysis Library

The SQLite MCP Server v2.6.0 includes a comprehensive statistical analysis library with 8 specialized functions for data analysis and business intelligence.

**📚 See [Performance Optimization Guide](https://gist.github.com/neverinfamous/bd95e9aec1040d7f8f81a356351da541) for complete statistical analysis workflows and advanced use cases.**

### Available Statistical Functions

**Descriptive Statistics:**
```javascript
descriptive_statistics({
  table_name: "sales_data",
  column_name: "revenue",
  where_clause: "year = 2024"  // optional
})
```
Returns comprehensive statistics including mean, median, standard deviation, variance, range, and coefficient of variation.

**Percentile Analysis:**
```javascript
percentile_analysis({
  table_name: "sales_data", 
  column_name: "revenue",
  percentiles: [25, 50, 75, 90, 95, 99]  // optional
})
```
Calculates quartiles, percentiles, and interquartile range (IQR) for distribution analysis.

**Time Series Analysis:**
```javascript
moving_averages({
  table_name: "daily_sales",
  value_column: "revenue", 
  time_column: "date",
  window_sizes: [7, 30, 90]  // optional
})
```
Generates moving averages with trend analysis for time series data.

### Statistical Analysis Workflow

1. **Explore Data Distribution**: Use `descriptive_statistics` to understand central tendency and variability
2. **Identify Quartiles**: Apply `percentile_analysis` to find data distribution boundaries  
3. **Analyze Trends**: Employ `moving_averages` for time series pattern recognition
4. **Generate Insights**: Combine statistical results with business context using `append_insight`

### Example Analysis Session

```javascript
// 1. Get overview of sales performance
descriptive_statistics({
  table_name: "monthly_sales",
  column_name: "revenue"
})

// 2. Understand distribution 
percentile_analysis({
  table_name: "monthly_sales", 
  column_name: "revenue",
  percentiles: [10, 25, 50, 75, 90]
})

// 3. Analyze trends over time
moving_averages({
  table_name: "monthly_sales",
  value_column: "revenue",
  time_column: "month", 
  window_sizes: [3, 6, 12]
})
```

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 🔍 Full-Text Search (FTS5)

The SQLite MCP Server provides comprehensive full-text search capabilities through its integrated FTS5 extension with dedicated management tools.

### FTS5 Management Tools

**Create FTS5 Tables:**
```javascript
create_fts_table({
  "table_name": "documents_fts",
  "columns": ["title", "content", "category"],
  "content_table": "documents",  // Optional: populate from existing table
  "tokenizer": "unicode61"       // Optional: unicode61, porter, ascii
})
```

**Enhanced Search with Ranking:**
```javascript
fts_search({
  "table_name": "documents_fts",
  "query": "database optimization",
  "limit": 10,
  "snippet_length": 50
})
// Returns: BM25 ranking, highlighted snippets, structured results
```

**Rebuild Indexes for Performance:**
```javascript
rebuild_fts_index({
  "table_name": "documents_fts"
})
```

### Manual Search Examples

```javascript
// Basic full-text search
read_query({
  "query": "SELECT * FROM documents_fts WHERE documents_fts MATCH 'integration' LIMIT 10"
})

// Phrase search with exact matching
read_query({
  "query": "SELECT * FROM documents_fts WHERE documents_fts MATCH '\"exact phrase\"'"
})
```

### Search Best Practices

- Use double quotes for exact phrase matching: `"exact phrase"`
- Use asterisk for prefix matching: `integrat*` (matches "integration", "integrate", etc.)
- Combine terms with AND/OR: `database AND design`, `sqlite OR postgres`
- Use the rank ordering for most relevant results first

### Advanced Search Techniques

The FTS5 extension supports advanced search techniques:

- **Phrase matching**: `"thread management"`
- **Boolean operators**: `cloudflare AND workers`
- **Prefix matching**: `cloud*`
- **Exclusion**: `NOT redis`
- **Combinations**: `"pattern analysis" NOT quantum`

For programmatic access, use the SQLite FTS5 interface with snippet highlighting:

```sql
-- Search with result highlighting
SELECT 
  id, title, 
  snippet(documents_fts, 0, '<em>', '</em>', '...', 15) AS snippet
FROM 
  documents_fts
WHERE 
  documents_fts MATCH 'search term'
ORDER BY 
  rank
LIMIT 10;
```

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 💾 Backup & Restore Operations

The SQLite MCP Server provides enterprise-grade backup and restore capabilities using SQLite's native backup API for atomic, consistent operations.

### Backup Operations

**Create Database Backups:**
```javascript
backup_database({
  "backup_path": "./backups/database_2025-09-16.db",
  "overwrite": false  // Optional: prevent accidental overwrites
})
```

**Verify Backup Integrity:**
```javascript
verify_backup({
  "backup_path": "./backups/database_2025-09-16.db"
})
// Returns: file size, integrity check, table count, version info
```

### Restore Operations

**Restore from Backup:**
```javascript
restore_database({
  "backup_path": "./backups/database_2025-09-16.db",
  "confirm": true  // Required for safety
})
```

### Safety Features

- **Confirmation Required**: All restore operations require explicit `confirm=true`
- **Pre-restore Backup**: Current database automatically backed up before restore
- **Integrity Verification**: Comprehensive backup validation before operations
- **Atomic Operations**: Uses SQLite backup API for consistent, reliable operations
- **Directory Creation**: Automatically creates backup directories as needed

---

## ⚙️ Advanced PRAGMA Operations

The SQLite MCP Server provides comprehensive PRAGMA management tools for database configuration, optimization, and introspection.

### Configuration Management

**Get/Set PRAGMA Settings:**
```javascript
pragma_settings({
  "pragma_name": "journal_mode"
})
// Returns: PRAGMA journal_mode = delete

pragma_settings({
  "pragma_name": "synchronous", 
  "value": "NORMAL"
})
// Sets and confirms: PRAGMA synchronous = NORMAL
```

### Performance Optimization

**Database Optimization:**
```javascript
pragma_optimize({
  "analysis_limit": 1000  // Optional: limit analysis scope
})
// Runs PRAGMA optimize for query performance improvements
```

### Database Introspection

**Detailed Table Information:**
```javascript
pragma_table_info({
  "table_name": "users",
  "include_foreign_keys": true  // Include FK and index info
})
// Returns: columns, foreign keys, indexes, constraints
```

**Database List:**
```javascript
pragma_database_list()
// Returns: all attached databases with file paths and schemas
```

**SQLite Capabilities:**
```javascript
pragma_compile_options()
// Returns: SQLite version, compile options, feature availability
```

### Supported PRAGMA Commands

- **Configuration**: journal_mode, synchronous, cache_size, temp_store
- **Performance**: optimize, analysis_limit, mmap_size  
- **Security**: foreign_keys, recursive_triggers, secure_delete
- **Debugging**: compile_options, database_list, table_info
- **And many more** - supports all SQLite PRAGMA commands

---

## 🛡️ Security & Data Integrity

**Enhanced Security Interface:** All query tools (`read_query`, `write_query`, `create_table`) now support optional parameter binding to prevent SQL injection attacks:

```javascript
// ✅ SECURE: Parameter binding prevents injection
read_query({
  "query": "SELECT * FROM users WHERE username = ? AND role = ?",
  "params": ["john_doe", "admin"]
})

// ✅ SECURE: Write operations with parameters  
write_query({
  "query": "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
  "params": ["Laptop", 999.99, "electronics"]
})

// ✅ v2.6.0: Enhanced automatic JSON serialization for objects/arrays
write_query({
  "query": "INSERT INTO table_name (json_data, tags) VALUES (?, ?)",
  "params": [{"key": "value", "nested": {"data": "example"}}, ["tag1", "tag2", "tag3"]]
})

// ✅ v2.6.0: JSON Helper Tools provide even simpler syntax
json_insert({
  "table": "table_name",
  "column": "json_data",
  "data": {"key": "value", "nested": {"data": "example"}}
})

// ✅ SECURE: Table creation with parameters
create_table({
  "query": "CREATE TABLE IF NOT EXISTS ? (id INTEGER PRIMARY KEY, name TEXT)",
  "params": ["dynamic_table"]
})
```

**Security Benefits:**
- 🛡️ **SQL Injection Prevention**: Malicious input treated as literal data, not executable code
- 🔄 **Backward Compatible**: Existing queries without params continue to work
- ⚡ **Performance**: Query plan caching and optimization
- 🎯 **Automatic JSON Handling**: Dict/list objects automatically serialized to JSON
- 📝 **Best Practice**: Follows secure coding standards


### JSONB Binary Storage

The SQLite MCP Server implements SQLite JSONB binary storage format for all JSON data, providing significant advantages:

- **Reduced Storage Size**: Estimated 15% space savings across migrated tables
- **Faster Parsing**: No need to re-parse JSON text for each operation
- **Type Preservation**: Binary format preserves data types without text conversion
- **Elimination of Escaping Issues**: No complex character escaping needed
- **Efficient Path Access**: Optimized for JSON path extraction operations

#### Usage:

For optimal JSON handling, SQLite automatically uses JSONB format internally. Simply provide JSON strings directly:

```javascript
// Insert JSON record directly (automatically uses JSONB internally)
write_query({
  "query": "INSERT INTO table_name (json_column) VALUES ('{\"key\": \"value\"}')"
})

// With parameter binding (for programmatic access)
write_query({
  "query": "INSERT INTO table_name (json_column) VALUES (?)",
  "params": [JSON.stringify({"key": "value"})]
})

// Query using standard JSON functions
read_query({
  "query": "SELECT json_extract(json_column, '$.key') FROM table_name"
})
```

Note: The explicit `jsonb()` function should only be used in specific advanced cases or when required for parameter binding pattern. For direct SQL statements, standard JSON strings work efficiently.

### Transaction Safety

All write operations are automatically wrapped in transactions with proper rollback on errors:

- **Automatic Transactions**: Every write operation is wrapped in a transaction
- **Error Rollback**: Failed operations automatically roll back changes
- **Data Integrity**: Ensures database consistency even during failures
- **Zero Configuration**: Works automatically without setup

### Foreign Key Enforcement

Automatic enforcement of foreign key constraints across all connections:

- **Referential Integrity**: Ensures data relationships remain valid
- **Cascade Operations**: Supports CASCADE, RESTRICT, SET NULL operations
- **Cross-Connection Consistency**: Enforced across all database connections
- **PRAGMA Support**: Uses SQLite's foreign_keys pragma for enforcement

---

## 🎯 JSON Helper Tools

*New in v2.6.0 - Complete JSON Operations Suite*

The SQLite MCP Server v2.6.0 introduces 6 specialized JSON helper tools that provide a complete abstraction layer over SQLite's JSON functions. These tools eliminate the complexity of writing raw JSON SQL and provide automatic parameter serialization, intelligent auto-normalization, and enhanced error diagnostics.

### 🚀 Key Capabilities

* **Direct JSON Operations**: Complete abstraction of complex SQLite JSON functions
* **Automatic Parameter Serialization**: Pass JavaScript objects directly without manual JSON.stringify()
* **Intelligent Auto-Normalization**: Automatic repair of common JSON formatting issues
* **Enhanced Error Diagnostics**: Contextual, actionable error messages with security alerts
* **Backward Compatibility**: Legacy SQL JSON operations continue to work unchanged
* **Performance Optimized**: Efficient JSON path validation and query building

### 🔧 Available JSON Helper Tools

#### **`json_insert`** - Insert JSON Data with Validation
Insert JSON data with automatic serialization and comprehensive validation:

```javascript
// Simple example - automatic serialization
json_insert({
  "table": "products",
  "column": "metadata",
  "data": {
    "name": "Laptop",
    "category": "electronics",
    "specs": {"cpu": "Intel i7", "ram": "16GB"}
  }
})
```

**📚 See [JSON Helper Tools Masterclass](https://gist.github.com/neverinfamous/6398e1af3109ed4846af5275b13dff5c) for complete JSON manipulation recipes and advanced use cases.**

#### **`json_update`** - Update JSON Fields by Path
Update specific JSON fields with precision targeting:

```javascript
// Update nested JSON values
json_update({
  "table": "products",
  "column": "metadata",
  "path": "$.specs.ram",
  "value": "32GB",
  "where_clause": "id = 123"
})
```

#### **`json_select`** - Extract JSON Data with Flexible Output
Extract JSON data with multiple output format options:

```javascript
// Extract specific paths
json_select({
  "table": "products",
  "column": "metadata", 
  "paths": ["$.name", "$.category", "$.specs.cpu"],
  "where_clause": "active = 1",
  "format": "objects"  // Options: objects, arrays, flat
})
```

#### **`json_query_complex`** - Advanced JSON Filtering
Advanced JSON filtering and querying operations:

```javascript
// Complex JSON-based filtering
json_query_complex({
  "table": "products",
  "column": "metadata",
  "filters": [
    {"path": "$.category", "operator": "=", "value": "electronics"},
    {"path": "$.specs.ram", "operator": ">=", "value": "16GB"}
  ],
  "logic": "AND"
})
```

#### **`json_merge`** - Intelligent JSON Object Merging
Merge JSON objects with configurable conflict resolution:

```javascript
// Merge with conflict resolution
json_merge({
  "table": "users",
  "column": "profile", 
  "merge_data": {
    "preferences": {"theme": "dark", "notifications": true}
  },
  "strategy": "deep_merge",
  "where_clause": "id = 456"
})
```

#### **`json_validate_security`** - Security-Focused JSON Validation
Advanced JSON validation with security threat detection:

```javascript
// Comprehensive security validation
json_validate_security({
  "json_data": '{"user": "admin", "permissions": ["read", "write"]}',
  "check_injection": true,
  "check_xss": true,
  "max_depth": 10
})
```

### 🔧 Fixes Automatically Applied

The JSON helper tools include intelligent auto-normalization that fixes common formatting issues:

* **Single to Double Quotes**: Converts `{'key': 'value'}` to `{"key": "value"}`
* **Python Booleans**: Converts `True/False/None` to `true/false/null`
* **Trailing Commas**: Removes invalid trailing commas from objects and arrays
* **Unquoted Keys**: Adds missing quotes around object keys
* **Mixed Quote Types**: Standardizes to double quotes throughout

```javascript
// These problematic formats are automatically fixed:
json_insert({
  "table": "users",
  "column": "profile", 
  "data": "{'name': 'John', 'active': True, 'data': None,}"  // Auto-normalized
})
// Becomes: {"name": "John", "active": true, "data": null}
```

### 🛡️ Enhanced Error Diagnostics

When JSON operations fail, get intelligent, contextual error messages:

* **Error Categorization**: Structural, security, or encoding issues
* **Specific Suggestions**: Actionable guidance for each error type  
* **Security Alerts**: Clear warnings for suspicious patterns
* **Context Information**: Shows what auto-normalization was attempted

### 🚀 Migration from Raw JSON SQL

**Before v2.6.0 (Complex SQL):**
```javascript
write_query({
  "query": "UPDATE products SET metadata = json_set(metadata, '$.category', ?, '$.tags', json(?)) WHERE id = ?",
  "params": ["electronics", JSON.stringify(["new", "popular"]), 123]
})
```

**After v2.6.0 (Simple Helper Tools):**
```javascript
json_update({
  "table": "products",
  "column": "metadata",
  "path": "$.category", 
  "value": "electronics",
  "where_clause": "id = 123"
})
```

### 🎯 Best Practices

1. **Use Helper Tools for New Development**: Take advantage of automatic serialization and validation
2. **Leverage Auto-Normalization**: Let the system fix common JSON formatting issues
3. **Enable Security Validation**: Use `json_validate_security` for user-supplied JSON
4. **Batch Operations**: Use `json_query_complex` for multiple JSON-based filters
5. **Consistent Error Handling**: Handle enhanced error diagnostics in your application logic

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## ✅ Best Practices for Using SQLite MCP

### Standard Query Workflow

1. Start with `list_tables` to identify available tables
   ```javascript
   list_tables()
   ```

2. For each relevant table, use `describe_table` to verify exact schema
   ```javascript
   describe_table({"table_name": "users"})
   ```

3. Based on verified schema, construct appropriate queries using exact column names
   ```javascript
   read_query({
     "query": "SELECT id, name, email FROM users WHERE status = 'active' ORDER BY created_at DESC LIMIT 5"
   })
   ```

4. When searching for specific content, use LIKE with wildcards (%) to increase match probability
   ```javascript
   read_query({
     "query": "SELECT id, project_type, description FROM projects WHERE description LIKE '%keyword%' ORDER BY last_updated DESC LIMIT 5"
   })
   ```

5. For JSON operations, use standard JSON strings for both direct queries and parameter binding
   ```javascript
   // Direct SQL with JSON string
   write_query({
     "query": "INSERT INTO table_name (json_data) VALUES ('{\"key\": \"value\"}')"
   })
   
   // With automatic JSON serialization (recommended)
   write_query({
     "query": "INSERT INTO table_name (json_data) VALUES (?)",
     "params": [{"key": "value"}]  // Objects automatically serialized to JSON
   })
   
   // Manual serialization (still supported)
   write_query({
     "query": "INSERT INTO table_name (json_data) VALUES (?)",
     "params": [JSON.stringify({"key": "value"})]
   })
   ```

### Example JSON Operations

```javascript
// Insert JSON record with automatic serialization (recommended)
write_query({
  "query": "INSERT INTO products (name, details, metadata) VALUES (?, ?, ?)",
  "params": ["Product A", "High-quality item", {"category": "electronics", "tags": ["new", "popular"]}]
})

// Extract value from JSON
read_query({
  "query": "SELECT json_extract(metadata, '$.tags[0]') FROM products WHERE name = ?",
  "params": ["Product A"]
})

// Update nested JSON value with parameters
write_query({
  "query": "UPDATE products SET metadata = json_set(metadata, '$.category', ?) WHERE id = ?",
  "params": ["updated_category", 123]
})

// Filter by JSON value with parameters
read_query({
  "query": "SELECT id, name FROM products WHERE json_extract(metadata, '$.category') = ?",
  "params": ["electronics"]
})
```

### SQLite-Specific Query Structure

- **Use SQLite-style PRIMARY KEY**: `INTEGER PRIMARY KEY` not `AUTO_INCREMENT`
- **Use TEXT for strings**: SQLite uses `TEXT` instead of `VARCHAR`
- **JSON storage is automatic**: Direct JSON strings are automatically stored efficiently
- **Use proper date functions**: SQLite date functions differ from MySQL
- **No enum type**: Use CHECK constraints instead of ENUM
- **No LIMIT with OFFSET**: Use `LIMIT x OFFSET y` syntax

### Correct Tool Usage Examples

#### SQLite Example

```javascript
// Get table list from SQLite
list_tables()

// Query data from SQLite
read_query({
  "query": "SELECT * FROM users LIMIT 5"
})

// Query with parameters (recommended for dynamic queries)
read_query({
  "query": "SELECT * FROM users WHERE status = ? LIMIT ?",
  "params": ["active", 5]
})

// Update data in SQLite with parameter binding (recommended)
write_query({
  "query": "UPDATE products SET metadata = ? WHERE id = ?",
  "params": ["{\"key\": \"value\"}", 123]
})

// Insert with multiple parameters
write_query({
  "query": "INSERT INTO users (name, email, status) VALUES (?, ?, ?)",
  "params": ["John Doe", "john@example.com", "active"]
})

// Get table structure in SQLite
describe_table({
  "table_name": "users"
})
```


[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 🔧 Troubleshooting

### JSONB-Specific Troubleshooting

If you encounter JSON-related errors:

1. **"no such function: jsonb"**: Your SQLite version doesn't support JSONB (requires 3.45.0+)
   ```javascript
   // Check SQLite version
   read_query({"query": "SELECT sqlite_version()"})
   ```

2. **"Invalid JSON in column"**: The JSON string is malformed
   ```javascript
   // Validate JSON first
   validate_json({"json_str": jsonString})
   ```

3. **"JSON parse error"**: JSON syntax is incorrect
   ```javascript
   // Use correct JSON format with double quotes
   // Incorrect: {'key': 'value'}
   // Correct: {"key": "value"}
   ```

### Transaction Safety Troubleshooting

1. **"database is locked"**: Another connection is holding the database lock
   - This error should be less common with transaction safety, but can still occur
   - Check for long-running transactions in other processes
   
2. **"Error during rollback"**: Problem occurred during transaction rollback
   - Check the database integrity
   - Restart the MCP server if persistent

### Foreign Key Troubleshooting

1. **"foreign key constraint failed"**: Attempted to violate a foreign key constraint
   - Verify the referenced record exists before inserting/updating
   - Use proper cascading delete where appropriate
   
2. **"PRAGMA foreign_keys error"**: Problem enabling foreign keys
   - This should not occur with the enhanced implementation
   - Check if using a compatible SQLite version

### Additional Troubleshooting Areas

1. **Database connectivity issues**:
   - Check file paths and permissions
   - Ensure SQLite database file is accessible
   - Verify database file is not corrupted

2. **Performance issues**:
   - Check database size and indexes
   - Consider running VACUUM for optimization
   - Review query complexity

3. **JSON data issues**:
   - Validate JSON strings before insertion
   - Use parameter binding for complex JSON data
   - Check for proper escaping in JSON strings

---

## 🗄️ Database Configuration

- **Auto-creates** `sqlite_mcp.db` in your project root if none exists because **MCP operations require persistent storage** between tool calls
- **Connects to existing databases** - works with any SQLite file you specify
- **Supports both relative and absolute paths** for maximum flexibility.

### Database Location Best Practices

- **`./data/sqlite_mcp.db`** - Recommended for projects (organized, version-control friendly)
- **`./sqlite_mcp.db`** - Simple option for small projects  
- **Existing databases** - Use `--db-path` to connect to any SQLite database
- **`:memory:`** - Temporary database for testing (data not persisted)

---

## 📊 Virtual Table Management

The SQLite MCP Server provides comprehensive virtual table management capabilities, supporting multiple virtual table types for specialized data access patterns and performance optimization.

### Virtual Table Management Tools

#### **create_rtree_table** - R-Tree Spatial Indexing
Create R-Tree virtual tables for efficient spatial queries and geometric data indexing.

```python
# Create a 2D spatial index for geographic data
create_rtree_table(
    table_name="locations_spatial",
    dimensions=2,
    coordinate_type="float"
)

# Create a 3D spatial index for volumetric data
create_rtree_table(
    table_name="objects_3d",
    dimensions=3,
    coordinate_type="float"
)
```

**Features:**
- Configurable dimensions (2D, 3D, multi-dimensional)
- Float or integer coordinate types
- Automatic column generation (id, min0, max0, min1, max1, etc.)
- Optimized for range queries and spatial searches

#### **create_csv_table** - CSV File Access
Create virtual tables that directly access CSV files with configurable parsing options.

```python
# Create a virtual table for a CSV file with headers
create_csv_table(
    table_name="sales_data",
    csv_file_path="/path/to/sales.csv",
    has_header=True,
    delimiter=","
)

# Create a virtual table for a TSV file without headers
create_csv_table(
    table_name="log_data",
    csv_file_path="/path/to/logs.tsv",
    has_header=False,
    delimiter="\t"
)
```

**Features:**
- Direct CSV file access without importing
- Configurable delimiters (comma, tab, pipe, etc.)
- Header row detection and handling
- Automatic fallback to temporary table if CSV extension unavailable

#### **create_series_table** - Sequence Generation
Create virtual tables that generate numeric sequences for testing, reporting, and data generation.

```python
# Create a simple number series
create_series_table(
    table_name="numbers_1_to_100",
    start_value=1,
    end_value=100,
    step=1
)

# Create a series with custom step
create_series_table(
    table_name="even_numbers",
    start_value=2,
    end_value=1000,
    step=2
)
```

**Features:**
- Configurable start, end, and step values
- Automatic fallback to regular table with recursive CTE
- Perfect for generating test data and sequences
- Memory-efficient virtual table implementation

#### **list_virtual_tables** - Virtual Table Discovery
List all virtual tables in the database with detailed type information.

```python
list_virtual_tables()
```

**Returns:**
- Virtual table names and SQL definitions
- Automatic type detection (rtree, fts, csv, generate_series)
- Complete virtual table inventory
- Structured JSON output with metadata

#### **virtual_table_info** - Schema Inspection
Get detailed information about specific virtual tables including column schemas and configuration.

```python
virtual_table_info(table_name="locations_spatial")
```

**Features:**
- Complete column information with types and constraints
- Virtual table type identification
- SQL definition display
- Column count and metadata

#### **drop_virtual_table** - Safe Removal
Safely remove virtual tables with confirmation requirements to prevent accidental data loss.

```python
# Safe drop with confirmation
drop_virtual_table(
    table_name="old_spatial_index",
    confirm=True
)
```

**Safety Features:**
- Mandatory confirmation flag to prevent accidents
- Virtual table verification before deletion
- Detailed status reporting
- Error handling for non-existent tables

### Performance Benefits

- **R-Tree Tables**: O(log n) spatial queries vs O(n) table scans
- **CSV Tables**: Direct file access without storage duplication
- **Series Tables**: Memory-efficient sequence generation
- **Comprehensive Management**: Centralized virtual table lifecycle control

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 🧠 Semantic/Vector Search

The SQLite MCP Server provides comprehensive semantic search capabilities, enabling AI-native applications with embedding storage, similarity search, and hybrid keyword+semantic ranking. This makes it perfect for recommendation systems, question-answering, and content discovery.

**📚 See [Vector/Semantic Search Complete Tutorial](https://gist.github.com/neverinfamous/b2d844e97c77090699ddd212331bedb4) for complete workflows, OpenAI/HuggingFace integration examples, and advanced use cases.**

### Quick Example

**Create embeddings table and store vectors:**
```javascript
// 1. Create table for embeddings
create_embeddings_table({
  "table_name": "documents",
  "embedding_dim": 1536
})

// 2. Store embedding with content
store_embedding({
  "table_name": "documents", 
  "embedding": [0.1, -0.3, 0.8, ...],
  "content": "Your document text here"
})

// 3. Search similar content
semantic_search({
  "table_name": "documents",
  "query_embedding": [0.2, -0.1, 0.9, ...],
  "limit": 5
})
```

**Available Tools:** `create_embeddings_table`, `store_embedding`, `semantic_search`, `hybrid_search`, `calculate_similarity`, `batch_similarity_search`

---

## 🌍 SpatiaLite Geospatial Analytics

The SQLite MCP Server provides enterprise-grade geospatial capabilities through SpatiaLite integration, transforming SQLite into a comprehensive GIS platform for location-based business intelligence and spatial data analysis.

**📚 See [SpatiaLite GIS Cookbook](https://gist.github.com/neverinfamous/86db4ce8e1ecd36692d96ca4abdc670f) for complete geospatial workflows and advanced GIS use cases.**

### Quick Example

**Load SpatiaLite and create spatial table:**
```javascript
// 1. Load SpatiaLite extension
load_spatialite()

// 2. Create spatial table
create_spatial_table({
  "table_name": "locations",
  "geometry_type": "POINT",
  "srid": 4326
})

// 3. Run spatial query
spatial_query({
  "query": "SELECT name FROM locations WHERE ST_Distance(geom, GeomFromText('POINT(-122.4 37.8)')) <= 1000"
})
```

**Available Tools:** `load_spatialite`, `create_spatial_table`, `spatial_index`, `spatial_query`, `geometry_operations`, `import_shapefile`, `spatial_analysis`

---

## 📋 Enhanced Virtual Tables

The SQLite MCP Server provides intelligent data import capabilities with automatic schema detection, type inference, and seamless conversion of CSV and JSON files into queryable SQLite tables.

**📚 See [Real-World Use Cases](https://gist.github.com/neverinfamous/7d36fb5676c5767e5c5aad4250244887) for complete CSV/JSON import workflows, schema inference examples, and data processing pipelines.**

### Quick Example

**Import CSV with automatic schema detection:**
```javascript
// 1. Analyze CSV structure
analyze_csv_schema({
  "csv_file_path": "./data/sales.csv"
})

// 2. Create enhanced virtual table
create_enhanced_csv_table({
  "table_name": "sales_data",
  "csv_file_path": "./data/sales.csv",
  "has_header": true
})

// 3. Query the data
read_query({
  "query": "SELECT * FROM sales_data WHERE amount > 1000"
})
```

**Available Tools:** `create_enhanced_csv_table`, `create_json_collection_table`, `analyze_csv_schema`, `analyze_json_schema`

---

## 🤖 Intelligent MCP Resources & Prompts

The SQLite MCP Server provides intelligent meta-awareness and guided workflows through advanced MCP Resources and Prompts, transforming it from a simple database interface into a self-aware, intelligent assistant.

### MCP Resources - Database Meta-Awareness

MCP Resources provide dynamic "knowledge hooks" that give the AI model instant access to database metadata without requiring repeated queries.

**Available Resources:**

**`database://schema`** - Complete database schema with natural language descriptions
**`database://capabilities`** - Real-time server capabilities and feature status  
**`database://statistics`** - Performance metrics and usage analytics
**`database://search_indexes`** - FTS5 and spatial index status with optimization suggestions
**`database://performance`** - Query performance analysis and bottleneck identification
**`memo://insights`** - Business insights memo (continuously updated)
**`diagnostics://json`** - JSON capabilities diagnostic information

### MCP Prompts - Guided Workflows

MCP Prompts provide intelligent workflow automation, acting as "recipes" that guide complex multi-step operations.

**Available Prompts:**

**`semantic_query`** - Natural language to semantic search translation  
**`summarize_table`** - Intelligent table analysis with configurable depth
**`optimize_database`** - Step-by-step database optimization workflow
**`setup_semantic_search`** - Complete guide for setting up semantic search
**`hybrid_search_workflow`** - Hybrid keyword + semantic search implementation
**`mcp-demo`** - Seed database with initial data and demonstrate capabilities
**`json-diagnostic`** - Check SQLite JSONB capabilities and run diagnostics

### Benefits of Resources & Prompts

- **Reduced Hallucination**: AI always has access to current database state through resources
- **Improved Workflows**: Complex operations are guided by proven prompt recipes  
- **Meta-Awareness**: Server becomes self-aware of its own capabilities and limitations
- **Consistency**: Standardized approaches to common database operations

---

## ✅ Best Practices for Using SQLite MCP

### Standard Query Workflow

1. **Explore Schema**: Use `list_tables()` and `describe_table()` to understand your data structure
2. **Query Data**: Use `read_query()` for SELECT operations with proper parameter binding
3. **Modify Data**: Use `write_query()` for INSERT/UPDATE/DELETE with parameter binding for security
4. **Capture Insights**: Use `append_insight()` to document discoveries for future reference

### Security Best Practices

1. **Always Use Parameter Binding**: Prevent SQL injection by using parameterized queries
2. **Validate JSON**: Use JSON validation tools before storing data
3. **Regular Backups**: Use the backup tools to maintain data integrity
4. **Monitor Performance**: Use PRAGMA operations to track database health

---

## ⚡ Vector Index Optimization

The SQLite MCP Server provides enterprise-grade vector index optimization with Approximate Nearest Neighbor (ANN) search capabilities, transforming vector similarity search from O(n) linear to O(log n) sub-linear performance for massive datasets.

### Vector Index Optimization Tools

**`create_vector_index`** - Build optimized indexes for lightning-fast vector search
```javascript
create_vector_index({
  "table_name": "embeddings_table",
  "embedding_column": "embedding",     // Column containing vector embeddings
  "index_type": "cluster",             // cluster (k-means), grid (spatial), hash (LSH)
  "num_clusters": 100,                 // Number of clusters for k-means indexing
  "grid_size": 10                      // Grid dimensions for spatial indexing
})
```

**`optimize_vector_search`** - Perform ultra-fast ANN search using created indexes
```javascript
optimize_vector_search({
  "table_name": "embeddings_table",
  "query_embedding": [0.1, 0.2, 0.3, ...],
  "limit": 10,                         // Maximum results to return
  "search_k": 5,                       // Clusters to search (accuracy vs speed)
  "similarity_threshold": 0.7          // Minimum similarity score
})
```

**`analyze_vector_index`** - Comprehensive index performance analysis
```javascript
analyze_vector_index({
  "table_name": "embeddings_table"
})
// Returns: index statistics, cluster distribution, performance estimates
```

**`rebuild_vector_index`** - Intelligent index maintenance and optimization
```javascript
rebuild_vector_index({
  "table_name": "embeddings_table",
  "force": false                       // Force rebuild even if current
})
```

### Performance Benefits

- **Faster Search**: Sub-linear O(log n) performance vs O(n) linear search
- **Massive Scalability**: Handle millions of embeddings efficiently
- **Intelligent Clustering**: K-means partitioning reduces candidates by 90%+
- **Configurable Accuracy**: Balance speed vs precision with search_k parameter
- **Pure SQLite**: No external dependencies or complex setup required

### Index Types

**Cluster Index (K-Means)**:
- Best for: General-purpose vector search with balanced performance
- Algorithm: K-means clustering partitions vector space intelligently
- Performance: Excellent for most embedding dimensions and data distributions

**Grid Index (Spatial)**:
- Best for: High-dimensional embeddings with uniform distribution
- Algorithm: Multi-dimensional spatial grid partitioning
- Performance: Optimal for embeddings with known bounds and even distribution

**Hash Index (LSH)**:
- Best for: Extremely high-dimensional sparse vectors
- Algorithm: Locality-Sensitive Hashing for approximate similarity
- Performance: Constant-time lookup with configurable precision

### Example Workflow

```javascript
// 1. Create optimized index for your embedding table
create_vector_index({
  "table_name": "document_embeddings", 
  "index_type": "cluster",
  "num_clusters": 50
})

// 2. Perform lightning-fast similarity search
optimize_vector_search({
  "table_name": "document_embeddings",
  "query_embedding": your_query_vector,
  "limit": 20,
  "search_k": 3
})

// 3. Monitor and optimize index performance
analyze_vector_index({"table_name": "document_embeddings"})

// 4. Rebuild index after adding new embeddings
rebuild_vector_index({"table_name": "document_embeddings"})
```

[⬆️ Back to Table of Contents](#-table-of-contents)

---

## 🤖 Intelligent MCP Resources & Prompts

The SQLite MCP Server provides intelligent meta-awareness and guided workflows through advanced MCP Resources and Prompts, transforming it from a simple database interface into a self-aware, intelligent assistant.

### MCP Resources - Database Meta-Awareness

MCP Resources provide dynamic "knowledge hooks" that give the AI model instant access to database metadata without requiring repeated queries.

**Available Resources:**

**`database://schema`** - Complete database schema with natural language descriptions
```javascript
// Automatically provides:
// - All table names and structures
// - Column types and constraints  
// - Row counts and relationships
// - Natural language schema summary
```

**`database://capabilities`** - Comprehensive server capabilities matrix
```javascript
// Provides real-time information about:
// - Available tools (73 total)
// - Feature support (FTS5, semantic search, virtual tables)
// - Advanced features and limitations
// - Server and SQLite versions
```

**`database://statistics`** - Real-time database statistics and health metrics
```javascript
// Dynamic statistics including:
// - Database size and page information
// - Table row counts and sizes
// - Index usage and efficiency
// - Performance recommendations
```

**`database://search_indexes`** - Search index status and capabilities
```javascript
// Comprehensive index information:
// - FTS5 tables and configurations
// - Semantic search embeddings status
// - Virtual table listings
// - Index optimization suggestions
```

**`database://performance`** - Performance analysis and optimization recommendations
```javascript
// Intelligent performance insights:
// - Health score assessment
// - Maintenance recommendations
// - Optimization suggestions
// - Best practices guidance
```

### MCP Prompts - Guided Workflows

MCP Prompts provide intelligent workflow automation, acting as "recipes" that guide complex multi-step operations.

**Available Prompts:**

**`semantic_query`** - Natural language to semantic search translation
- Guides the AI through converting natural language questions into proper semantic search operations
- Handles embedding generation, similarity thresholds, and result interpretation
- Provides fallback strategies for complex queries

**`summarize_table`** - Intelligent table analysis with configurable depth
- Automated table exploration with statistical analysis
- Configurable analysis depth (quick, standard, deep)
- Generates natural language summaries with key insights

**`optimize_database`** - Step-by-step database optimization workflow  
- Comprehensive optimization checklist
- Automated VACUUM, ANALYZE, and integrity checking
- Performance tuning recommendations

**`setup_semantic_search`** - Complete semantic search implementation guide
- End-to-end setup for embedding tables and indexes
- Integration with external embedding services
- Testing and validation procedures

**`hybrid_search_workflow`** - Hybrid keyword + semantic search implementation
- Combines FTS5 keyword search with semantic similarity
- Configurable weighting between search methods
- Result ranking and relevance tuning

### Benefits of Resources & Prompts

**Reduced Hallucination**: AI always has access to current database state through resources  
**Improved Workflows**: Complex operations are guided by proven prompt recipes  
**Meta-Awareness**: Server becomes self-aware of its own capabilities and limitations  
**Consistency**: Standardized approaches to common database operations  
**Efficiency**: Eliminates repetitive queries for metadata and schema information

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

## 🔒 Security

If you discover a security vulnerability, please follow our [Security Policy](SECURITY.md) for responsible disclosure.

---

## 🔗 Additional Resources

- **[Testing Guide](../tests/README.md)** - Comprehensive testing documentation
- **[Contributing](../CONTRIBUTING.md)** - How to contribute to the project
- **[Security Policy](../SECURITY.md)** - Security guidelines and reporting
- **[Code of Conduct](../CODE_OF_CONDUCT.md)** - Community guidelines
- **[Docker Hub](https://hub.docker.com/r/writenotenow/sqlite-mcp-server)** - Container images
- **[GitHub Releases](https://github.com/neverinfamous/sqlite-mcp-server/releases)** - Version history
- **[Adamic Support Blog](https://adamic.tech/)** - Project announcements and releases

---

## 💬 Support

- 📝 [Open an issue](https://github.com/neverinfamous/mcp_server_sqlite/issues) for bug reports or feature requests
- 🌐 Visit memory-journal-mcp (https://github.com/neverinfamous/memory-journal-mcp)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 🏷️ Attribution

Based on the original SQLite MCP Server by the [Model Context Protocol team](https://github.com/modelcontextprotocol/servers) (MIT License).

[⬆️ Back to Table of Contents](#-table-of-contents)

---