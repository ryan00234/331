/**
 * Created by work on 2017/4/11.
 */
         var pieData = [
                {
                    value: 30,
                    color:"#F38630"
                },
                {
                    value : 50,
                    color : "#E0E4CC"
                },
                {
                    value : 100,
                    color : "#69D2E7"
                }

            ];

    var myPie = new Chart(document.getElementById("canvas2").getContext("2d")).Pie(pieData);

    var options = {
        //Boolean - If we show the scale above the chart data
        // 网格线是否在数据线的上面
        scaleOverlay : false,

        //Boolean - If we want to override with a hard coded scale
        // 是否用硬编码重写y轴网格线
        scaleOverride : false,

        //** Required if scaleOverride is true **
        //Number - The number of steps in a hard coded scale
        // y轴刻度的个数
        scaleSteps : null,
        //Number - The value jump in the hard coded scale
        // y轴每个刻度的宽度
        scaleStepWidth : null,
        //Number - The scale starting value
        // y轴的起始值
        scaleStartValue : null,

        //String - Colour of the scale line
        // x轴y轴的颜色
        scaleLineColor : "rgba(0,0,0,1)",

        //Number - Pixel width of the scale line
        // x轴y轴的线宽
        scaleLineWidth : 1,

        //Boolean - Whether to show labels on the scale
        // 是否显示y轴的标签
        scaleShowLabels : true,

        //Interpolated JS string - can access value
        // 标签显示值
        scaleLabel : "<%=value%>",

        //String - Scale label font declaration for the scale label
        // 标签的字体
        scaleFontFamily : "'Arial'",

        //Number - Scale label font size in pixels
        // 标签字体的大小
        scaleFontSize : 12,

        //String - Scale label font weight style
        // 标签字体的样式
        scaleFontStyle : "normal",

        //String - Scale label font colour
        // 标签字体的颜色
        scaleFontColor : "#666",

        ///Boolean - Whether grid lines are shown across the chart
        // 是否显示网格线
        scaleShowGridLines : true,

        //String - Colour of the grid lines
        // 网格线的颜色
        scaleGridLineColor : "rgba(0,0,0,.1)",

        //Number - Width of the grid lines
        // 网格线的线宽
        scaleGridLineWidth : 1,

        //Boolean - Whether the line is curved between points
        // 是否是曲线
        bezierCurve : true,

        //Boolean - Whether to show a dot for each point
        // 是否显示点
        pointDot : true,

        //Number - Radius of each point dot in pixels
        // 点的半径
        pointDotRadius : 3,

        //Number - Pixel width of point dot stroke
        // 点的线宽
        pointDotStrokeWidth : 1,

        //Boolean - Whether to show a stroke for datasets
        datasetStroke : true,

        //Number - Pixel width of dataset stroke
        // 数据线的线宽
        datasetStrokeWidth : 2,

        //Boolean - Whether to fill the dataset with a colour
        // 数据线是否填充颜色
        datasetFill : true,

        //Boolean - Whether to animate the chart
        // 是否有动画效果
        animation : true,

        //Number - Number of animation steps
        // 动画的步数
        animationSteps : 60,

        //String - Animation easing effect
        // 动画的效果
        animationEasing : "easeOutQuart",

        //Function - Fires when the animation is complete
        // 动画完成后调用
        onAnimationComplete : null
    }

    Pie.defaults = {
    //Boolean - Whether we should show a stroke on each segment
    // 块和块之间是否有间距
    segmentShowStroke : true,

    //String - The colour of each segment stroke
　　// 块和块之间间距的颜色
    segmentStrokeColor : "#fff",

    //Number - The width of each segment stroke
　　// 块和块之间间距的宽度
    segmentStrokeWidth : 2,

    //Boolean - Whether we should animate the chart
    animation : true,

    //Number - Amount of animation steps
    animationSteps : 100,

    //String - Animation easing effect
    animationEasing : "easeOutBounce",

    //Boolean - Whether we animate the rotation of the Pie
　　// 是否有从0度到360度的动画
    animateRotate : true,

    //Boolean - Whether we animate scaling the Pie from the centre
　　// 是否有从中心到边缘的动画
    animateScale : false,

    //Function - Will fire on animation completion.
    onAnimationComplete : null
}