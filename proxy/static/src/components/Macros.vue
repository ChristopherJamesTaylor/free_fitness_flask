<template>
<div>
<Menu></Menu>


  <div id="DPG">

<div class="dpg-calculator macros-calculator">
<h2 class="dpg-h2 calc-header">Macronutrient Calculator</h2>
<div class="calc-container"><span class="calc-subheader">Age</span>
<div class="calc-row"><input type="text" class="bbTextBox calc-textbox" name="age" placeholder="Years" value=""></div>
<span class="calc-subheader">Sex</span>
<div class="calc-row"><input type="radio" id="macros-male" name="sex" value="M" checked="checked"> <label class="calc-label-small" for="macros-male"><span></span>Male</label> <input type="radio" id="macros-female" name="sex" value="F"> <label class="calc-label-small calc-float-right" for="macros-female"><span></span>Female</label></div>
<span class="calc-subheader">Height</span>
<div class="calc-row"><input type="radio" id="macros-feet" name="height-system" value="feet" checked="checked"> <label class="calc-label-small" for="macros-feet"><span></span>Feet</label> <input type="radio" id="macros-meters" name="height-system" value="meters"> <label class="calc-label-small calc-float-right" for="macros-meters"><span></span>Meters</label></div>
<div class="calc-row"><input type="text" class="bbTextBox calc-textbox-half" name="height-tens" placeholder="Feet" value=""> <input type="text" class="bbTextBox calc-textbox-half calc-float-right" name="height-units" placeholder="Inches" value=""></div>
<span class="calc-subheader">Weight</span>
<div class="calc-row"><input type="radio" id="macros-pounds" name="weight-system" value="pounds" checked="checked"> <label class="calc-label-small" for="macros-pounds"><span></span>Pounds</label> <input type="radio" id="macros-kilos" name="weight-system" value="kilos"> <label class="calc-label-small calc-float-right" for="macros-kilos"><span></span>Kilograms</label></div>
<div class="calc-row"><input type="text" name="weight" class="bbTextBox calc-textbox" placeholder="Pounds"></div>
<span class="calc-subheader">Goal</span>
<div class="calc-row"><input type="radio" id="macros-goal1" name="goal" value="fat-loss" checked="checked"> <label class="calc-label" for="macros-goal1"><span></span>Fat Loss</label></div>
<div class="calc-row"><input type="radio" id="macros-goal2" name="goal" value="maintenance"> <label class="calc-label" for="macros-goal2"><span></span>Maintenance</label></div>
<div class="calc-row"><input type="radio" id="macros-goal3" name="goal" value="gainz"> <label class="calc-label" for="macros-goal3"><span></span>Muscle Gainz</label></div>
<span class="calc-subheader">Activity Level</span>
<div class="calc-row"><input type="radio" id="macros-activity1" name="activity" value="L" checked="checked"> <label class="calc-label" for="macros-activity1"><span></span>Lightly active (moderate exercise but sedentary job)</label></div>
<div class="calc-row"><input type="radio" id="macros-activity2" name="activity" value="M"> <label class="calc-label" for="macros-activity2"><span></span>Moderately active (intense exercise but sedentary job)</label></div>
<div class="calc-row"><input type="radio" id="macros-activity3" name="activity" value="V"> <label class="calc-label" for="macros-activity3"><span></span>Very active (moderate exercise and active job)</label></div>
<div class="calc-row"><input type="radio" id="macros-activity4" name="activity" value="E"> <label class="calc-label" for="macros-activity4"><span></span>Extra active (intense exercise and active job)</label></div>
<button class="bb-flat-btn calc-submit" type="button">Calculate</button>
<h3 class="dpg-h3 calc-answer"></h3>
</div>
</div>

</div>
</div>
</template>

<script>
  import Menu from './Menu'
  export default {
    name: 'Macros',
    components: {Menu}
  }
</script>

<style scoped>

</style>
