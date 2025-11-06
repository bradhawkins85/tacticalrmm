# Test Plan for Client/Site Search Feature

## Test Environment Setup

1. Clone and build the tacticalrmm-web repository with the modifications
2. Ensure you have sample data with multiple clients and sites
3. Navigate to the Dashboard view

## Recommended Test Data

For thorough testing, ensure your test environment has:
- At least 5 clients with varying names
- Each client should have 2-5 sites
- Mix of client/site names with:
  - Common words (e.g., "Office", "HQ", "Main")
  - Unique identifiers (e.g., "Acme Corp", "Beta LLC")
  - Different cases (e.g., "GAMMA Inc", "delta services")

## Test Cases

### TC-01: Search Field Visibility
**Objective**: Verify search field is visible and properly positioned

**Steps**:
1. Navigate to Dashboard
2. Look at the left navigation panel

**Expected Results**:
- [ ] Search input field is visible above the client tree
- [ ] Search field has a search icon on the left
- [ ] Placeholder text reads "Search Clients/Sites..."
- [ ] Field is properly styled (outlined, dense)

---

### TC-02: Search by Client Name (Exact Match)
**Objective**: Verify exact client name search works

**Steps**:
1. Type a complete client name in the search field (e.g., "Acme Corp")

**Expected Results**:
- [ ] Only the matching client appears in the tree
- [ ] All sites under that client are visible
- [ ] Non-matching clients are hidden
- [ ] Tree structure is maintained

---

### TC-03: Search by Client Name (Partial Match)
**Objective**: Verify partial client name search works

**Steps**:
1. Type part of a client name (e.g., "acme" for "Acme Corp")

**Expected Results**:
- [ ] Matching client(s) appear in the tree
- [ ] All sites under matching clients are visible
- [ ] Search is case-insensitive
- [ ] Partial matches work correctly

---

### TC-04: Search by Site Name
**Objective**: Verify site name search works

**Steps**:
1. Type a site name that belongs to a specific client (e.g., "HQ")

**Expected Results**:
- [ ] Parent client(s) appear in the tree
- [ ] Only matching site(s) are visible under each client
- [ ] Non-matching sites are hidden
- [ ] If multiple clients have sites with the same name, all are shown

---

### TC-05: Case Insensitivity
**Objective**: Verify search is case-insensitive

**Steps**:
1. Type "ACME" (uppercase)
2. Clear and type "acme" (lowercase)
3. Clear and type "AcMe" (mixed case)

**Expected Results**:
- [ ] All three searches return the same results
- [ ] "Acme Corp" appears in all cases
- [ ] Case of search input doesn't affect results

---

### TC-06: No Results Found
**Objective**: Verify behavior when no matches are found

**Steps**:
1. Type a string that doesn't match any client or site (e.g., "zzzzz")

**Expected Results**:
- [ ] Tree shows empty state
- [ ] "All Clients" option remains visible
- [ ] No errors are thrown
- [ ] Interface remains responsive

---

### TC-07: Clear Search
**Objective**: Verify clear button functionality

**Steps**:
1. Type a search term to filter the tree
2. Click the clear button (X) in the search field

**Expected Results**:
- [ ] Search field is cleared
- [ ] All clients and sites are visible again
- [ ] Tree returns to original state
- [ ] Clear button disappears when field is empty

---

### TC-08: Manual Clear (Delete All Text)
**Objective**: Verify clearing by deleting text

**Steps**:
1. Type a search term
2. Manually delete all characters using backspace

**Expected Results**:
- [ ] As characters are deleted, more results appear
- [ ] When field is empty, all clients/sites are visible
- [ ] Filtering updates in real-time

---

### TC-09: Real-time Filtering
**Objective**: Verify filtering happens as user types

**Steps**:
1. Slowly type "acme" one character at a time: "a" → "ac" → "acm" → "acme"

**Expected Results**:
- [ ] Results update after each character
- [ ] No need to press Enter or click a button
- [ ] Filtering is smooth and responsive
- [ ] No noticeable lag

---

### TC-10: Multiple Matches
**Objective**: Verify behavior when multiple items match

**Steps**:
1. Type a common word that appears in multiple clients/sites (e.g., "office")

**Expected Results**:
- [ ] All matching clients appear
- [ ] All matching sites appear under their respective clients
- [ ] Original tree structure is maintained
- [ ] Sorting by alert severity is preserved among matches

---

### TC-11: Special Characters
**Objective**: Verify search handles special characters

**Steps**:
1. Search for client/site with special characters (e.g., "Acme & Co", "Site-01")

**Expected Results**:
- [ ] Special characters in names are handled correctly
- [ ] Matching works with hyphens, ampersands, etc.
- [ ] No errors or unexpected behavior

---

### TC-12: Whitespace Handling
**Objective**: Verify whitespace in search terms

**Steps**:
1. Type "Acme Corp" (with space)
2. Type " office " (with leading/trailing spaces)

**Expected Results**:
- [ ] Spaces in search terms work correctly
- [ ] Matching accounts for spaces in names
- [ ] Leading/trailing spaces don't break functionality

---

### TC-13: Tree Interaction After Filtering
**Objective**: Verify tree remains interactive after filtering

**Steps**:
1. Search for a specific client
2. Try to expand/collapse the client node
3. Right-click for context menu
4. Click on a site

**Expected Results**:
- [ ] Expand/collapse works normally
- [ ] Context menu appears correctly
- [ ] Clicking sites loads agents
- [ ] All tree interactions work as expected

---

### TC-14: Search Persistence During Navigation
**Objective**: Verify search state

**Steps**:
1. Enter a search term
2. Click on a filtered client/site
3. Observe the search field

**Expected Results**:
- [ ] Search term remains in field
- [ ] Filtered view is maintained
- [ ] User can continue refining search

---

### TC-15: "All Clients" Selection with Active Search
**Objective**: Verify "All Clients" button behavior with search

**Steps**:
1. Enter a search term to filter results
2. Click "All Clients" button

**Expected Results**:
- [ ] "All Clients" is selected
- [ ] Filtered results remain filtered
- [ ] Agent table shows all agents from filtered clients
- [ ] Expected behavior per application design

---

### TC-16: Performance with Many Clients
**Objective**: Verify performance with large datasets

**Prerequisites**: Test environment with 50+ clients, each with 5+ sites

**Steps**:
1. Type various search terms
2. Observe responsiveness

**Expected Results**:
- [ ] Search remains responsive
- [ ] No noticeable lag when typing
- [ ] Filtering completes quickly (< 100ms)
- [ ] UI doesn't freeze or stutter

---

### TC-17: Accessibility
**Objective**: Verify keyboard and screen reader accessibility

**Steps**:
1. Tab to search field using keyboard
2. Type search term
3. Tab through filtered results

**Expected Results**:
- [ ] Search field is keyboard accessible
- [ ] Focus indicator is visible
- [ ] Tab order is logical
- [ ] Screen readers announce the field properly

---

### TC-18: Visual Consistency
**Objective**: Verify visual design consistency

**Steps**:
1. Observe search field styling
2. Compare with other UI elements
3. Test in light and dark modes (if applicable)

**Expected Results**:
- [ ] Search field matches application design language
- [ ] Styling is consistent with other Quasar components
- [ ] Icons are properly sized and aligned
- [ ] Works in both light and dark themes

---

## Regression Tests

### RT-01: Original Functionality Preserved
**Objective**: Ensure existing features still work

**Steps**:
1. Clear search field
2. Test all original tree operations

**Expected Results**:
- [ ] Tree sorting by alert severity works
- [ ] Context menus work
- [ ] Add client/site functions work
- [ ] Tree expansion/collapse works
- [ ] All original features are intact

---

### RT-02: Agent Table Unaffected
**Objective**: Verify agent table continues to work

**Steps**:
1. Filter clients using search
2. Click on a filtered client/site
3. Observe agent table

**Expected Results**:
- [ ] Agent table displays correctly
- [ ] Agent table search is independent
- [ ] Both searches can be used simultaneously
- [ ] No conflicts between tree and table search

---

## Bug Reports Template

If issues are found during testing, use this template:

```
**Test Case**: TC-XX
**Summary**: [Brief description]
**Steps to Reproduce**:
1. Step one
2. Step two
3. ...

**Expected Result**: [What should happen]
**Actual Result**: [What actually happened]
**Severity**: [Critical/High/Medium/Low]
**Browser/Environment**: [Browser version, OS, etc.]
**Screenshots**: [If applicable]
```

---

## Success Criteria

The feature is considered ready for production when:
- [ ] All test cases pass
- [ ] No critical or high severity bugs
- [ ] Performance is acceptable (< 100ms for filtering)
- [ ] Accessibility requirements are met
- [ ] Visual design is approved
- [ ] Code review is complete
- [ ] Documentation is updated

---

## Test Sign-off

**Tested By**: ___________________
**Date**: ___________________
**Environment**: ___________________
**Result**: [ ] PASS / [ ] FAIL
**Notes**: 
_______________________________________________
_______________________________________________
