# Client/Site Search Feature - Quick Start

## 🔍 New Feature: Search/Filter for Client/Site Navigation

This fork includes an enhancement to the Tactical RMM web interface that adds a search/filter field to the left-hand navigation panel, making it easier to find specific Clients or Sites.

### Why This Feature?

As the number of clients grows, it becomes increasingly difficult to locate the correct entry in the navigation panel, especially since the list is currently sorted by alert severity rather than alphabetically. This feature solves that problem.

### What's Included

This repository contains complete documentation and implementation files for adding a search field to the tacticalrmm-web frontend:

📄 **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Start here! Complete overview of the feature

📂 **web-frontend-changes/** - All files needed to implement the feature:
- `DashboardView.vue` - Modified frontend component
- `client-site-search.patch` - Git patch for easy application
- `README.md` - Detailed technical documentation
- `VISUAL_MOCKUP.md` - Visual examples and use cases
- `TEST_PLAN.md` - Comprehensive testing guide

📋 **[FRONTEND_SEARCH_FEATURE.md](FRONTEND_SEARCH_FEATURE.md)** - Implementation guide

### Quick Start

1. **Read the Summary**: Start with [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
2. **Choose Your Method**: Pick one of three ways to apply changes:
   - Apply the patch file
   - Copy the modified file
   - Manual implementation
3. **Test**: Use the comprehensive test plan in `web-frontend-changes/TEST_PLAN.md`
4. **Deploy**: Build and deploy your modified frontend

### How It Works

```
┌────────────────────────┐
│ 🔍 [Search box]       │  ← Type here to filter
├────────────────────────┤
│ 📁 All Clients         │
│ 🏢 Acme Corp          │  ← Only matching
│    🏠 HQ              │     clients/sites
│ 🏢 Beta LLC           │     appear
│    🏠 Office          │
└────────────────────────┘
```

### Features

- ✅ **Real-time filtering** - Results update as you type
- ✅ **Case-insensitive** - "ACME" and "acme" both work
- ✅ **Smart filtering** - Searches both client and site names
- ✅ **Clear button** - Quickly reset to show all
- ✅ **No backend changes** - All filtering happens in browser
- ✅ **Maintains compatibility** - No breaking changes

### Repository Structure

```
tacticalrmm/                          # Main backend repository
├── IMPLEMENTATION_SUMMARY.md         # Overview and quick start
├── FRONTEND_SEARCH_FEATURE.md        # Implementation guide
└── web-frontend-changes/             # Frontend implementation
    ├── DashboardView.vue             # Modified component
    ├── client-site-search.patch      # Git patch
    ├── README.md                     # Technical docs
    ├── VISUAL_MOCKUP.md              # Visual examples
    └── TEST_PLAN.md                  # Testing guide

tacticalrmm-web/                      # Frontend repository (separate)
└── src/views/DashboardView.vue       # ← This file gets modified
```

### Need Help?

- **Full Documentation**: See [web-frontend-changes/README.md](web-frontend-changes/README.md)
- **Visual Examples**: See [web-frontend-changes/VISUAL_MOCKUP.md](web-frontend-changes/VISUAL_MOCKUP.md)
- **Testing Guide**: See [web-frontend-changes/TEST_PLAN.md](web-frontend-changes/TEST_PLAN.md)

### About Tactical RMM

For information about the main Tactical RMM project, see the [official repository](https://github.com/amidaware/tacticalrmm) and [documentation](https://docs.tacticalrmm.com).

---

**Note**: This feature modifies the frontend (tacticalrmm-web repository). No backend changes are required.
