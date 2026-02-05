# Code Refactoring with Architecture Patterns - Commands

## Overview
Use GitHub Copilot commands to refactor code to modern architecture patterns.

## Slash Commands

### /fix - Apply Refactoring

**Usage:**
```
Select legacy code and use:
/fix Refactor this to use the Repository pattern with dependency injection
```

### /simplify - Reduce Complexity

**Usage:**
```
Select complex code and use:
/simplify Break this into smaller, single-responsibility functions
```

### /doc - Document Architecture

**Usage:**
```
/doc Explain the architecture pattern used in this code and create a diagram
```

## Demo Workflow

### Step 1: Identify Code Smell (1 minute)
```
@workspace Find classes with more than 200 lines that violate single responsibility principle
```

### Step 2: Select Pattern (1 minute)
```
Which architecture pattern would be best for this code?
Options: Repository, MVC, Observer, Factory, Strategy
```

### Step 3: Refactor (3 minutes)
```
/fix Refactor this monolithic class to use [chosen pattern]
```

### Step 4: Verify (2 minutes)
```
/tests Generate tests to verify the refactored code maintains the same behavior
```

### Step 5: Document (1 minute)
```
/doc Create documentation explaining the refactoring and the architecture pattern used
```

## Advanced Refactoring Commands

### Extract Interface
```
Select a class and use inline chat:
Extract an interface from this class and update all dependencies to use the interface
```

### Dependency Injection
```
/fix Add dependency injection to this class using constructor injection
```

### Separate Concerns
```
/fix This class has multiple responsibilities. Split it into separate classes following SRP
```

### Apply SOLID Principles
```
Refactor this code to follow SOLID principles
```
