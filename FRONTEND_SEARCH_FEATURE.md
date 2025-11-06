# Client/Site Search Feature - Implementation Guide

## Overview

This document describes the implementation of a search/filter field for the left-hand navigation panel in Tactical RMM's web interface. This feature addresses the need to quickly find specific Clients or Sites as the number of clients grows.

## Problem Addressed

- Growing number of clients makes it difficult to locate specific entries
- Current list is sorted by alert severity, not alphabetically
- No quick way to filter or search for specific clients/sites

## Solution Implemented

A search input field has been added above the client/site tree in the left navigation panel, providing:
- Real-time filtering as users type
- Case-insensitive search
- Search across both client and site names
- Smart filtering (shows clients with all sites if client matches, or only matching sites if only sites match)

## Files Modified

### Frontend Repository (tacticalrmm-web)

**File**: `src/views/DashboardView.vue`

Changes include:
1. Added search input field in the template
2. Added `treeSearch` data property for storing search query
3. Added `filteredClientsTree` computed property for filtering logic
4. Updated tree component to use filtered results

## Applying the Changes

### Option 1: Using the Patch File

If you have a fork of the tacticalrmm-web repository:

```bash
cd your-tacticalrmm-web-repo
git apply /path/to/web-frontend-changes/client-site-search.patch
```

### Option 2: Manual Implementation

If you prefer to make changes manually:

1. Open `src/views/DashboardView.vue` in your tacticalrmm-web repository
2. Refer to the complete modified file in `web-frontend-changes/DashboardView.vue`
3. Or follow the detailed changes in `web-frontend-changes/README.md`

### Option 3: Using the Complete Modified File

```bash
cp web-frontend-changes/DashboardView.vue your-tacticalrmm-web-repo/src/views/
```

## Building and Deploying

After applying the changes:

```bash
cd your-tacticalrmm-web-repo
npm install
npm run build
```

Then deploy the built frontend according to your Tactical RMM deployment process.

## Testing the Feature

1. Start the Tactical RMM web interface
2. Navigate to the Dashboard
3. Look for the search field in the left navigation panel (above the client tree)
4. Test the following:
   - Type a client name → Should show that client with all its sites
   - Type a site name → Should show parent client with only that site
   - Type partial matches → Should work (e.g., "corp" matches "Acme Corp")
   - Clear the search → Should show all clients/sites again
   - Test case-insensitivity → "ACME" and "acme" should both work

## Feature Characteristics

- **User Experience**: Clean, intuitive search interface
- **Performance**: Client-side filtering for instant results
- **Backward Compatibility**: No breaking changes, purely additive feature
- **No Backend Changes**: All filtering happens in the frontend
- **Maintains Existing Behavior**: Original sorting by alert severity is preserved

## Related Files

- `web-frontend-changes/DashboardView.vue` - Complete modified file
- `web-frontend-changes/client-site-search.patch` - Git patch file
- `web-frontend-changes/README.md` - Detailed implementation documentation

## Future Enhancements

Possible improvements for future iterations:
- Add keyboard shortcuts (e.g., Ctrl+F to focus search)
- Save search state in browser localStorage
- Add advanced filtering options (by status, by custom fields, etc.)
- Highlight matching text in results

## Support

For questions or issues with this feature, refer to:
- The detailed README in `web-frontend-changes/README.md`
- The patch file showing all changes
- The Tactical RMM community Discord/forums
