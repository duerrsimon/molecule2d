<script lang="ts">
  import { afterUpdate, onMount } from "svelte";

  // this is where it fails
  import SmilesDrawer from "smiles-drawer";

  export let smiles = "";

  onMount(() => {
    //   const SETTINGS = {
    //     width: 300,
    //     height: 200,
    //   };
    //   let drawer = new SmilesDrawer.SvgDrawer(SETTINGS);
    //   let svgElement;
    //   afterUpdate(() => {
    //     SmilesDrawer.parse(smiles, function (tree) {
    //       drawer.draw(tree, svgElement, "light");
    //     });
    //   });
  });
</script>

<div>
  <!-- <svg bind:this={svgElement} data-smiles={smiles} /> -->

  {smiles}
</div>
