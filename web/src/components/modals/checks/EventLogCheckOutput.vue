<template>
  <q-card style="min-width: 90vw" class="q-pa-xs">
    <q-card-section>
      <div class="row items-center">
        <div class="text-h6">{{ evtlogdata.desc }}</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </div>
      <div v-if="evtlogdata.extra_details !== null">
        <q-table
          dense
          class="remote-bg-tbl-sticky"
          :data="evtlogdata.extra_details.log"
          :columns="columns"
          :pagination.sync="pagination"
          row-key="uid"
          binary-state-sort
          virtual-scroll
          no-data-label="No event logs"
        />
      </div>
      <div v-else>Check has not run yet</div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "EventLogCheckOutput",
  props: ["evtlogdata"],
  data() {
    return {
      pagination: {
        rowsPerPage: 0,
        sortBy: "time",
        descending: true
      },
      columns: [
        { name: "eventType", label: "Type", field: "eventType", align: "left", sortable: true },
        { name: "source", label: "Source", field: "source", align: "left", sortable: true },
        { name: "eventID", label: "Event ID", field: "eventID", align: "left", sortable: true },
        { name: "time", label: "Time", field: "time", align: "left", sortable: true },
        { name: "message", label: "Message", field: "message", align: "left", sortable: true }
      ]
    };
  },
  beforeDestroy() {
    this.$emit("close");
  }
};
</script>