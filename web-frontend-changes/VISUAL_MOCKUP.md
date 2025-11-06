# Client/Site Search Feature - Visual Mockup

## Before (Original Layout)

```
┌─────────────────────────────────────────────┐
│  Tactical RMM Dashboard                     │
└─────────────────────────────────────────────┘
┌──────────────┬──────────────────────────────┐
│              │                              │
│  📁 All      │                              │
│    Clients   │     Agent Table              │
│              │                              │
│  🏢 Acme     │                              │
│    Corp      │                              │
│    🏠 HQ     │                              │
│    🏠 Branch │                              │
│              │                              │
│  🏢 Beta     │                              │
│    LLC       │                              │
│    🏠 Office │                              │
│              │                              │
│  🏢 Gamma    │                              │
│    Inc       │                              │
│    🏠 Main   │                              │
│    🏠 Remote │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

**Problem**: With many clients, users must scroll through the entire list to find a specific client or site.

---

## After (With Search Feature)

```
┌─────────────────────────────────────────────┐
│  Tactical RMM Dashboard                     │
└─────────────────────────────────────────────┘
┌──────────────┬──────────────────────────────┐
│ ┌──────────┐ │                              │
│ │🔍 Search │ │ ← NEW SEARCH FIELD           │
│ └──────────┘ │                              │
│              │                              │
│  📁 All      │                              │
│    Clients   │     Agent Table              │
│              │                              │
│  🏢 Acme     │                              │
│    Corp      │                              │
│    🏠 HQ     │                              │
│    🏠 Branch │                              │
│              │                              │
│  🏢 Beta     │                              │
│    LLC       │                              │
│    🏠 Office │                              │
│              │                              │
│  🏢 Gamma    │                              │
│    Inc       │                              │
│    🏠 Main   │                              │
│    🏠 Remote │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

**Solution**: A search field above the tree allows instant filtering.

---

## Usage Example 1: Searching for a Client

User types "beta" in the search field:

```
┌──────────────┬──────────────────────────────┐
│ ┌──────────┐ │                              │
│ │🔍 beta  ✕│ │ ← User typed "beta"          │
│ └──────────┘ │                              │
│              │                              │
│  📁 All      │                              │
│    Clients   │     Agent Table              │
│              │                              │
│  🏢 Beta     │ ← Only matching client shown │
│    LLC       │                              │
│    🏠 Office │ ← All sites of Beta shown    │
│              │                              │
│              │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

Result: Only "Beta LLC" is shown with all its sites.

---

## Usage Example 2: Searching for a Site

User types "remote" in the search field:

```
┌──────────────┬──────────────────────────────┐
│ ┌──────────┐ │                              │
│ │🔍 remote✕│ │ ← User typed "remote"        │
│ └──────────┘ │                              │
│              │                              │
│  📁 All      │                              │
│    Clients   │     Agent Table              │
│              │                              │
│  🏢 Gamma    │ ← Parent client shown        │
│    Inc       │                              │
│    🏠 Remote │ ← Only matching site shown   │
│              │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

Result: "Gamma Inc" is shown with only the "Remote" site.

---

## Usage Example 3: Partial Match

User types "corp" in the search field:

```
┌──────────────┬──────────────────────────────┐
│ ┌──────────┐ │                              │
│ │🔍 corp  ✕│ │ ← User typed "corp"          │
│ └──────────┘ │                              │
│              │                              │
│  📁 All      │                              │
│    Clients   │     Agent Table              │
│              │                              │
│  🏢 Acme     │ ← "Corp" matches             │
│    Corp      │                              │
│    🏠 HQ     │ ← All sites shown            │
│    🏠 Branch │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

Result: Partial string matching works (case-insensitive).

---

## Features

- **Real-time filtering**: Results update as you type
- **Case-insensitive**: "ACME", "acme", and "Acme" all match
- **Smart filtering**: 
  - Client name match → Shows client with all sites
  - Site name match → Shows client with only matching sites
- **Clear button**: Click ✕ to clear search and show all
- **No backend changes**: All filtering happens in browser
- **Preserves sorting**: Maintains alert severity sorting within results

---

## Technical Implementation

### Search Input Component
```vue
<q-input
  v-model="treeSearch"
  dense
  outlined
  clearable
  placeholder="Search Clients/Sites..."
  class="q-mb-sm"
>
  <template v-slot:prepend>
    <q-icon name="search" />
  </template>
</q-input>
```

### Filtering Logic (Simplified)
```javascript
filteredClientsTree() {
  if (!this.treeSearch) return this.clientsTree;
  
  const searchLower = this.treeSearch.toLowerCase();
  
  return this.clientsTree
    .map(client => {
      const clientMatches = client.label.toLowerCase().includes(searchLower);
      const filteredSites = client.children.filter(site =>
        site.label.toLowerCase().includes(searchLower)
      );
      
      if (clientMatches || filteredSites.length > 0) {
        return {
          ...client,
          children: clientMatches ? client.children : filteredSites
        };
      }
      return null;
    })
    .filter(client => client !== null);
}
```
