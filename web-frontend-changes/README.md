# Frontend Changes for Client/Site Search Feature

## Overview

This directory contains the modified frontend file to add a search/filter field to the left-hand navigation panel in the Tactical RMM web interface.

## Problem Statement

As the number of clients grows, it becomes increasingly difficult to locate the correct entry in the left-hand navigation panel, especially since the list is currently sorted by alert severity rather than alphabetically.

## Solution

Added a search input field above the client/site tree that allows users to quickly filter and find specific Clients or Sites by name.

## Changes Made

### File Modified: `src/views/DashboardView.vue`

The modified file is included in this directory: `DashboardView.vue`

### Key Changes:

1. **Added Search Input Field** (Lines 21-32)
   - Added a `q-input` component with search icon above the client tree
   - Styled with `dense` and `outlined` properties
   - Includes a clearable button to quickly reset the search
   - Placeholder text: "Search Clients/Sites..."

2. **Added `treeSearch` Data Property** (Line 486)
   - New reactive property to store the search query
   - Initialized as an empty string

3. **Added `filteredClientsTree` Computed Property** (Lines 898-927)
   - Filters the client tree based on the search query
   - Case-insensitive search that matches both client and site names
   - Smart filtering logic:
     - If a client name matches, shows the client with all its sites
     - If only site names match, shows the client with only matching sites
     - If neither match, hides the client entirely

4. **Updated Tree Component Binding** (Line 47)
   - Changed `:nodes="clientsTree"` to `:nodes="filteredClientsTree"`
   - This ensures the tree displays filtered results when searching

## How It Works

1. User types in the search field
2. The `treeSearch` data property updates in real-time
3. The `filteredClientsTree` computed property automatically recalculates
4. The tree component re-renders with filtered clients/sites
5. Clearing the search field (via clear button or deleting text) shows all clients/sites again

## Installation Instructions

To apply these changes to the tacticalrmm-web frontend:

1. Fork or clone the `amidaware/tacticalrmm-web` repository
2. Replace `src/views/DashboardView.vue` with the modified file from this directory
3. Build and deploy the frontend following the standard tacticalrmm-web build process

Alternatively, you can apply the changes manually by referring to the diff between the original and modified files.

## Testing

To test the functionality:

1. Navigate to the dashboard
2. Look for the new search field above the client/site tree in the left panel
3. Type a client or site name
4. Verify that:
   - Matching clients/sites appear in the tree
   - Non-matching items are filtered out
   - Partial matches work (e.g., "acme" matches "Acme Corp")
   - Search is case-insensitive
   - Clearing the search shows all clients/sites again

## Benefits

- **Faster Navigation**: Quickly locate specific clients or sites without scrolling
- **User-Friendly**: Simple, intuitive search interface
- **Smart Filtering**: Shows relevant results at both client and site levels
- **Non-Intrusive**: Doesn't affect existing functionality, just adds a new capability
- **Efficient**: Client-side filtering ensures fast, responsive search

## Technical Notes

- The search is implemented client-side for better performance
- No backend API changes are required
- The original tree sorting (by alert severity) is preserved
- The search works in conjunction with the existing tree structure
