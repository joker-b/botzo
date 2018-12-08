---
layout: post
title: "Special Ks (B)"
categories: [Botzilla]
tags: [Javascript, Algorithms]
---

<canvas width="700" height="350" id="km_sample2B" class="align-center">
</canvas>

<script>
	var sample2B = {
		pts: null,
		m: null,
		canvas: null,
		ctx: null,
		thisSample: null,
		iter: 0,
		paused: false,
		//
		sat_random_color: function() {
			// returns some strong color. We consider RG&B to be evenly-tempered, no perceptual hijinks
			var c = [Math.random(), Math.random(), Math.random()];
			var v = Math.max.apply(Math,c);
			c = c.map(function(x) { return Math.min(1.0, x/v);});
			var v = 1.0 - Math.min.apply(Math,c);
			c = c.map(function(x) { return Math.max(0.0, (1.0-x)/v);});
			c = c.map(function(x) { return Math.min(255, Math.floor(255*x));});
			return c;
		},
		init_sample2B_data: function(nPoints, mMeans) {
			// define a bunch of points, ten randomly place a few mean candidates
			var i, j;
			var inset = 0.1;
			var i2 = 1.0 - inset*2;
			// distribute points in device-normalized space, just in case we get resized
			this.pts = [];
			var xf = Math.PI/4 + Math.random()*8;
			var yf = Math.PI/4 + Math.random()*4;
			var xo = Math.PI * Math.random();
			var yo = Math.PI * Math.random();
			var lumpy = (Math.random() > 0.3);
			var dens = 1.0;
			var noise = 0.01;
			var nr = 1.0-noise;
			while (this.pts.length < nPoints) {
				var x = Math.random();
				var y = Math.random();
				if (lumpy) {
					dens = noise + nr * (0.5  + 0.5*Math.cos(xo + x*xf)) * (0.5  + 0.5*Math.cos(yo + y*yf));
				}
				if (Math.random() <= dens) {
					this.pts.push({
						x: inset+i2*x,
						y: inset+i2*y,
						m: 0			// altered by update_membership()
					});
				}
			}
			// likewise means -- these ones have an ANGLE because they only see what's in front of them
			this.m = [];
			for (i=0; i<mMeans; i=i+1) {
				var cv = this.sat_random_color();
				var angle = Math.random()*2*Math.PI;
				this.m.push({
					x: Math.random(),
					y: Math.random(),
					view_direction: {x:Math.cos(angle), y:Math.cos(angle)},
					cv: cv,
					c: ('rgb('+cv.join(',')+')'),
					active: true
				});
			}
		},
		vis_distance: function(p,m) {
			// distance betwee a point and a mean.
			// "True" Euclidena distance would include a square root,
			//     but we only care about relative ranking between points, so it's unneeded here.
			// We also don't need a specific magnitude for our dot product: just the sign
			var delta = {x: p.x-m.x, y: p.y-m.y };
			var dot = delta.x*m.view_direction.x + delta.y*m.view_direction.y;
			if (dot<0.0) {
				return -1; // not visible
			}
			var d = delta.x*delta.x + delta.y*delta.y;
			return d;

		},
		draw_points: function() {
			// draw points AND means
			var ip, im, ct;
			var w = this.canvas.width;
			var h = this.canvas.height;
			var mSize = 2;
			var mRad = 4;
			var mVec = 0.03;
			var gradient = this.ctx.createLinearGradient(0,0,w,h);
			gradient.addColorStop(0, 'white');
			gradient.addColorStop(.5, '#dddddd');
			gradient.addColorStop(1, 'white');
			this.ctx.fillStyle = gradient;
			this.ctx.fillRect(0,0,w,h)
			gradient = this.ctx.createLinearGradient(w,0,0,h);
			gradient.addColorStop(0, '#808080');
			gradient.addColorStop(.5, '#a0a0a0');
			gradient.addColorStop(1, '#808080');
			this.ctx.strokeStyle = gradient;
			this.ctx.beginPath();
			this.ctx.rect(0,0,w,h);
			this.ctx.stroke();
			for (im=0; im<this.m.length; im=im+1) {
				if (!this.m[im].active)
					continue;
				ct = 0;
				for (ip=0; ip<this.pts.length; ip=ip+1) {
					if ((this.pts[ip].m == im) || (this.pts[ip].m === null)) {
						ct += 1;
						var a = 1; // use this later
						var p = {x: (this.pts[ip].x * w),
							     y: (this.pts[ip].y * h)};
						this.ctx.strokeStyle = (this.pts[ip].m === null) ? '#d0d0d0' : ('rgba('+this.m[im].cv.join(',')+','+a+')');
						this.ctx.beginPath();
						this.ctx.moveTo(p.x-mSize, p.y-mSize);
						this.ctx.lineTo(p.x+mSize, p.y+mSize);
						this.ctx.stroke();
						this.ctx.beginPath();
						this.ctx.moveTo(p.x-mSize, p.y+mSize);
						this.ctx.lineTo(p.x+mSize, p.y-mSize);
						this.ctx.stroke();
					}
				}
				var pm = {x: this.m[im].x*w, y: this.m[im].y*h};
				this.ctx.strokeStyle = this.m[im].c;
				this.ctx.fillStyle = ('rgba('+this.m[im].cv.join(',')+',0.25)');
				this.ctx.beginPath();
				this.ctx.ellipse(pm.x, pm.y, mRad,mRad, Math.PI / 4, 0, 2 * Math.PI);
				this.ctx.fill();
				this.ctx.stroke();
				this.ctx.beginPath();
				this.ctx.moveTo(pm.x, pm.y);
				this.ctx.lineTo(pm.x+mVec*this.m[im].view_direction.x*w, pm.y+mVec*this.m[im].view_direction.y*h);
				this.ctx.stroke();
			}
		},
		update_memberships: function() {
			// update points, to see if any have switched affiliations. Return a count of
			//     how many have changed.
			var ip, im;
			var nChanged = 0;
			for (ip=0; ip<this.pts.length; ip=ip+1) {
				var dBest = 2; // some large value beyond our 1x1 space
				var mBest = null;
				for (im=0; im<this.m.length; im=im+=1) {
					if (!this.m[im].active)
						continue;
					var dm = this.vis_distance(this.pts[ip],this.m[im]);
					if ((dm>0)&&(dm<dBest)) {
						dBest = dm;
						mBest = im;
					}
				}
				if (mBest != this.pts[ip].m) {
					nChanged += 1;
					this.pts[ip].m = mBest;
				}
			}
			// console.log(nChanged+' changed');
			return(nChanged);
		},
		update_centroids: function() {
			// update mean locations (ignore inactive means)
			var ip, im, n, c, delta;
			for (im=0; im<this.m.length; im+=1) {
				if (!this.m[im].active)
					continue;
				n = 0;
				c = {x:0, y:0};
				aim = {x:0, y:0};
				// if we just move the location to the centroid of our member points, we'd surely
				//    push some behind our view. So instead, first let's do our best to aim at them.
				for (ip=0; ip<this.pts.length; ip+=1) {
					if (this.pts[ip].m == im) {
						n+=1;
						delta = {x: this.pts[ip].x-this.m[im].x, y: this.pts[ip].y-this.m[im].y};
						var dn = Math.sqrt(delta.x*delta.x + delta.y*delta.y); // normalize
						aim.x += (delta.x / dn);
						aim.y += (delta.y / dn);
					}
				}
				if (n==0) { // point set is EMPTY - mean can be deactivated
					this.m[im].actve = false;
					continue;
				}
				var aimd = Math.sqrt(aim.x*aim.x+aim.y*aim.y);
				this.m[im].view_direction.x = aim.x/aimd;
				this.m[im].view_direction.y = aim.y/aimd;
				// if we move the mean point to the centroid, some points are BEHIND us, so let's
				// go ther and then back up along our view axis
				for (ip=0; ip<this.pts.length; ip+=1) {
					if (this.pts[ip].m == im) {
						c.x += this.pts[ip].x;
						c.y += this.pts[ip].y;
					}
				}
				speed = 0.1;
				this.m[im].x += speed * (c.x/n - this.m[im].x);
				this.m[im].y += speed * (c.y/n - this.m[im].y);
				// now let's back up
				var dp = 12.0; // some larger-than-the-rnage value
				for (ip=0; ip<this.pts.length; ip+=1) {
					delta = {x: this.pts[ip].x-this.m[im].x, y: this.pts[ip].y-this.m[im].y};
					var f = this.m[im].view_direction.x * delta.x + this.m[im].view_direction.y * delta.y;
					if (f < dp) {
						dp = f;
					}
				}
				dp *= 0.15;
				this.m[im].x += dp * this.m[im].view_direction.x;
				this.m[im].y += dp * this.m[im].view_direction.y;

			}
		},
		update_all: function() {
			// our complete method -- just loop on this until you don't
			var m = this.update_memberships();
			if (m > 0) {
				this.update_centroids();
			}
			return(m);
		},
		remove_one: function() {
			// randomly remove a mean, until we reach some minimum
			var i, ct;
			for (i=0; i<this.m.length; i+=1) {
				if (this.m[i].active) {
					this.m[i].active = false;
					break;
				}
			}
			for (i=0, ct=0; i<this.m.length; i+=1) {
				if (this.m[i].active) {
					ct += 1;
				}
			}
			return (ct > 2);
		},
		looper: function(timestamp) {
			// called by requestAnimationFrame() forever
			if (this.paused) {
				window.requestAnimationFrame(this.looper.bind(this));
				return;
			}
			var ch = this.update_all();
			this.draw_points();
			if ((ch > 0)&&(this.iter < 200)) {
				window.requestAnimationFrame(this.looper.bind(this));
			} else if (this.remove_one()) {
				this.iter = 0;
				window.setTimeout(this.looper.bind(this),200);
			} else {
				window.setTimeout(this.startup.bind(this),100);
			}
			this.iter += 1;
		},
		startup: function() {
			// also called whenever we re-start
			this.init_sample2B_data(500,12);
			this.iter = 0;
			window.requestAnimationFrame(this.looper.bind(this));
		},
		toggle_pause: function() {
			// user can click to stop/start the animation
			this.paused = ! this.paused;
		},
		main: function(canvID) {
			this.canvas = document.getElementById(canvID);
			var p = this.canvas.parentElement;
			if (p.offsetWidth < (this.canvas.width-4)) {
				this.canvas.width = p.offsetWidth - 4;
			}
			this.ctx = this.canvas.getContext('2d');
			this.startup();
			this.canvas.onclick = this.toggle_pause.bind(this);
		}
	};
	// window.onload = function s2() {sample2B.main("km_sample2B"); };
	window.addEventListener('load', function s2() {sample2B.main("km_sample2B"); });
</script>

A follow-on to the [last post on _k-Means_]({{ site.baseurl}}{% post_url 2018-12-05-K-Means %}) &mdash; this time, we use different criteria to determine "closeness" and to adjust where we move things around.

<!--more-->

For this behavior, we add a "view direction" to each mean point (the pointer): it can only consider the points in front of it, each like a little fish-eyed security camera.

Overall the method is much like before, but with a bit more frenetic results:

* Look at every point, and mark it "owned" by the closest "mean" _that's aimed towards the point._
* _Aim_ each mean toward the middle of its "owned" points, and move it slightly "back" from the middle of their location.
* Repeat as before.

As with many "generative" methods, it fascinates me that such simple rules can give rise to complex behaviors that we usually ascribe to animals with some intelligence. In this case, the mean objects behave as if they are "tendng" or "herding" their data. There's even an illusion of cooperation and competition, like humminbirds at a feeder or wasps buzzing around a nest. An sense of organization though there's no _explicit_ connection between the different means.

Suggested soundtrack: Philip Glass, _Einstein on the Beach._

Next up: didn't I say this would get around to photography?

